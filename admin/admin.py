from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner

from collections import OrderedDict
from utlis.dataable import DataTable
from datetime import datetime
import mysql.connector
import hashlib

class AdminWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mydb = mysql.connector.connect(
            user='root',
            password='824582',
            host='127.0.0.1',
            database='pos'
        )
        self.mycursor = self.mydb.cursor()

        content = self.ids.scrn_contents
        users = self.get_users()
        userstable = DataTable(table=users)
        content.add_widget(userstable)

        # Display Products
        product_scrn = self.ids.scrn_product_content
        products = self.get_products()
        prod_table = DataTable(table=products)
        product_scrn.add_widget(prod_table)

    def add_user_fields(self):
        target = self.ids.ops_fields  # This is for the users screen
        target.clear_widgets()
        #---------------------------------
        self.crud_first = TextInput(hint_text='First Name')
        self.crud_last = TextInput(hint_text='Last Name')
        self.crud_user = TextInput(hint_text='User Name')
        self.crud_pwd = TextInput(hint_text='Password', password=True)
        self.crud_des = Spinner(text='Operator', values=['Operator', 'Administrator'])
        crud_submit = Button(text='Add', size_hint_x=None, width=100, on_release=self.add_user)

        target.add_widget(self.crud_first)
        target.add_widget(self.crud_last)
        target.add_widget(self.crud_user)
        target.add_widget(self.crud_pwd)
        target.add_widget(self.crud_des)
        target.add_widget(crud_submit)

    def add_user(self, instance):
        first = self.crud_first.text
        last = self.crud_last.text
        user = self.crud_user.text
        pwd = self.crud_pwd.text
        des = self.crud_des.text

        mydb = mysql.connector.connect(
            user='root',
            password='824582',
            host='127.0.0.1',
            database='pos'
        )
        mycursor = mydb.cursor()

        sql = "INSERT INTO users (first_name,last_name,user_name,password_,designation,date_) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (first, last, user, pwd, des, datetime.now())
        mycursor.execute(sql, val)
        mydb.commit()

        content = self.ids.scrn_contents
        content.clear_widgets()

        users = self.get_users()
        userstable = DataTable(table=users)
        content.add_widget(userstable)

    def update_user_fields(self):
        target = self.ids.ops_fields  # This is for the users screen
        target.clear_widgets()
        #----------------------------------
        self.crud_id = TextInput(hint_text='User ID')
        self.crud_first = TextInput(hint_text='First Name')
        self.crud_last = TextInput(hint_text='Last Name')
        self.crud_user = TextInput(hint_text='User Name')
        self.crud_pwd = TextInput(hint_text='Password', password=True)
        self.crud_des = Spinner(text='Operator', values=['Operator', 'Administrator'])
        crud_submit = Button(text='Update', size_hint_x=None, width=100, on_release=self.update_user)

        target.add_widget(self.crud_id)
        target.add_widget(self.crud_first)
        target.add_widget(self.crud_last)
        target.add_widget(self.crud_user)
        target.add_widget(self.crud_pwd)
        target.add_widget(self.crud_des)
        target.add_widget(crud_submit)

    def update_user(self, instance):
        user_id = self.crud_id.text
        first = self.crud_first.text
        last = self.crud_last.text
        user = self.crud_user.text
        pwd = self.crud_pwd.text
        des = self.crud_des.text

        mydb = mysql.connector.connect(
            user='root',
            password='824582',
            host='127.0.0.1',
            database='pos'
        )
        mycursor = mydb.cursor()

        sql = """
        UPDATE users
        SET first_name = %s, last_name = %s, user_name = %s, password_ = %s, designation = %s, date_ = %s
        WHERE id = %s
        """
        val = (first, last, user, pwd, des, datetime.now(), user_id)
        mycursor.execute(sql, val)
        mydb.commit()

        content = self.ids.scrn_contents
        content.clear_widgets()

        users = self.get_users()
        userstable = DataTable(table=users)
        content.add_widget(userstable)

    def remove_user_fields(self):
        target = self.ids.ops_fields  # This is for the users screen
        target.clear_widgets()
        #-----------------------------------
        self.crud_id = TextInput(hint_text='User ID')
        crud_submit = Button(text='Remove', size_hint_x=None, width=100, on_release=self.remove_user)

        target.add_widget(self.crud_id)
        target.add_widget(crud_submit)

    def remove_user(self, instance):
        user_id = self.crud_id.text

        mydb = mysql.connector.connect(
            user='root',
            password='824582',
            host='127.0.0.1',
            database='pos'
        )
        mycursor = mydb.cursor()

        sql = "DELETE FROM users WHERE id = %s"
        val = (user_id,)
        mycursor.execute(sql, val)
        mydb.commit()

        content = self.ids.scrn_contents
        content.clear_widgets()

        users = self.get_users()
        userstable = DataTable(table=users)
        content.add_widget(userstable)

    def add_product_fields(self):
        target = self.ids.ops_fields
        target.clear_widgets()
        self.prod_code = TextInput(hint_text='Product Code')
        self.prod_name = TextInput(hint_text='Product Name')
        self.prod_weight = TextInput(hint_text='Product Weight')
        self.prod_stock = TextInput(hint_text='Stock')
        self.prod_sold = TextInput(hint_text='Sold')
        self.prod_order = TextInput(hint_text='Order')
        self.prod_last_purchase = TextInput(hint_text='Last Purchase')
        crud_submit = Button(text='Add', size_hint_x=None, width=100, on_release=self.add_product)

        target.add_widget(self.prod_code)
        target.add_widget(self.prod_name)
        target.add_widget(self.prod_weight)
        target.add_widget(self.prod_stock)
        target.add_widget(self.prod_sold)
        target.add_widget(self.prod_order)
        target.add_widget(self.prod_last_purchase)
        target.add_widget(crud_submit)

    def add_product(self, instance):
        code = self.prod_code.text
        name = self.prod_name.text
        weight = self.prod_weight.text
        stock = self.prod_stock.text
        sold = self.prod_sold.text
        order = self.prod_order.text
        last_purchase = self.prod_last_purchase.text

        mydb = mysql.connector.connect(
            user='root',
            password='824582',
            host='127.0.0.1',
            database='pos'
        )
        mycursor = mydb.cursor()

        sql = "INSERT INTO stocks (product_code, product_name, product_weight, in_stock, sold, order, last_purchase) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (code, name, weight, stock, sold, order, last_purchase)
        mycursor.execute(sql, val)
        mydb.commit()

        content = self.ids.scrn_product_content
        content.clear_widgets()

        products = self.get_products()
        prod_table = DataTable(table=products)
        content.add_widget(prod_table)

    def update_product_fields(self):
        target = self.ids.ops_fields
        target.clear_widgets()
        self.prod_id = TextInput(hint_text='Product ID')
        self.prod_code = TextInput(hint_text='Product Code')
        self.prod_name = TextInput(hint_text='Product Name')
        self.prod_weight = TextInput(hint_text='Product Weight')
        self.prod_stock = TextInput(hint_text='Stock')
        self.prod_sold = TextInput(hint_text='Sold')
        self.prod_order = TextInput(hint_text='Order')
        self.prod_last_purchase = TextInput(hint_text='Last Purchase')
        crud_submit = Button(text='Update', size_hint_x=None, width=100, on_release=self.update_product)

        target.add_widget(self.prod_id)
        target.add_widget(self.prod_code)
        target.add_widget(self.prod_name)
        target.add_widget(self.prod_weight)
        target.add_widget(self.prod_stock)
        target.add_widget(self.prod_sold)
        target.add_widget(self.prod_order)
        target.add_widget(self.prod_last_purchase)
        target.add_widget(crud_submit)

    def update_product(self, instance):
        prod_id = self.prod_id.text
        code = self.prod_code.text
        name = self.prod_name.text
        weight = self.prod_weight.text
        stock = self.prod_stock.text
        sold = self.prod_sold.text
        order = self.prod_order.text
        last_purchase = self.prod_last_purchase.text

        mydb = mysql.connector.connect(
            user='root',
            password='824582',
            host='127.0.0.1',
            database='pos'
        )
        mycursor = mydb.cursor()

        sql = """
        UPDATE stocks
        SET product_code = %s, product_name = %s, product_weight = %s, in_stock = %s, sold = %s, order = %s, last_purchase = %s
        WHERE id = %s
        """
        val = (code, name, weight, stock, sold, order, last_purchase, prod_id)
        mycursor.execute(sql, val)
        mydb.commit()

        content = self.ids.scrn_product_content
        content.clear_widgets()

        products = self.get_products()
        prod_table = DataTable(table=products)
        content.add_widget(prod_table)

    def remove_product_fields(self):
        target = self.ids.ops_fields
        target.clear_widgets()
        self.prod_id = TextInput(hint_text='Product ID')
        crud_submit = Button(text='Remove', size_hint_x=None, width=100, on_release=self.remove_product)

        target.add_widget(self.prod_id)
        target.add_widget(crud_submit)

    def remove_product(self, instance):
        prod_id = self.prod_id.text

        mydb = mysql.connector.connect(
            user='root',
            password='824582',
            host='127.0.0.1',
            database='pos'
        )
        mycursor = mydb.cursor()

        sql = "DELETE FROM stocks WHERE id = %s"
        val = (prod_id,)
        mycursor.execute(sql, val)
        mydb.commit()

        content = self.ids.scrn_product_content
        content.clear_widgets()

        products = self.get_products()
        prod_table = DataTable(table=products)
        content.add_widget(prod_table)


    def get_users(self):
        mydb = mysql.connector.connect(
            user='root',
            password='824582',
            host='127.0.0.1',
            database='pos'
        )
        mycursor = mydb.cursor()
        _users = OrderedDict()
        _users['first_names'] = {}
        _users['last_names'] = {}
        _users['user_names'] = {}
        _users['passwords'] = {}
        _users['designations'] = {}
        first_names = []
        last_names = []
        user_names = []
        passwords = []
        designations = []
        sql = 'SELECT * FROM users'
        mycursor.execute(sql)
        users = mycursor.fetchall()
        for user in users:
            first_names.append(user[1])
            last_names.append(user[2])
            user_names.append(user[3])
            pwd = user[4]
            if len(pwd) > 10:
                pwd = pwd[:10] + '...'
            passwords.append(pwd)
            designations.append(user[5])

        users_length = len(first_names)
        idx = 0
        while idx < users_length:
            _users['first_names'][idx] = first_names[idx]
            _users['last_names'][idx] = last_names[idx]
            _users['user_names'][idx] = user_names[idx]
            _users['passwords'][idx] = passwords[idx]
            _users['designations'][idx] = designations[idx]
            idx += 1
        
        return _users

    def get_products(self):
        mydb = mysql.connector.connect(
            user='root',
            password='824582',
            host='127.0.0.1',
            database='pos'
        )
        mycursor = mydb.cursor()
        _stocks = OrderedDict()
        _stocks['product_code'] = {}
        _stocks['product_name'] = {}
        _stocks['product_weight'] = {}
        _stocks['in_stock'] = {}
        _stocks['sold'] = {}
        _stocks['order'] = {}
        _stocks['last_purchase'] = {}

        product_code = []
        product_name = []
        product_weight = []
        in_stock = []
        sold = []
        order = []
        last_purchase = []
        sql = 'SELECT * FROM stocks'
        mycursor.execute(sql)
        products = mycursor.fetchall()
        for product in products:
            product_code.append(product[1])
            name = product[2]
            if len(name) > 10:
                name = name[:10] + '...'
            product_name.append(name)
            product_weight.append(product[3])
            in_stock.append(product[5])
            sold.append(product[6])
            order.append(product[7])
            last_purchase.append(product[8])

        products_length = len(product_code)
        idx = 0
        while idx < products_length:
            _stocks['product_code'][idx] = product_code[idx]
            _stocks['product_name'][idx] = product_name[idx]
            _stocks['product_weight'][idx] = product_weight[idx]
            _stocks['in_stock'][idx] = in_stock[idx]
            _stocks['sold'][idx] = sold[idx]
            _stocks['order'][idx] = order[idx]
            _stocks['last_purchase'][idx] = last_purchase[idx]
            idx += 1
        
        return _stocks
        
    def change_screen(self, instance):
        if instance.text == 'Manage Products':
            self.ids.scrn_mngr.current = 'scrn_product_content'
        elif instance.text == 'Manage Users':
            self.ids.scrn_mngr.current = 'scrn_content'
        else:
            self.ids.scrn_mngr.current = 'scrn_analysis'


class AdminApp(App):
    def build(self):
        return AdminWindow()

if __name__ == '__main__':
    AdminApp().run()