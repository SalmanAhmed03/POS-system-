from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.label import Label
import re  # Import the re module

# Load the kv file explicitly
Builder.load_file('oper.kv')

class OperatorWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cart = []
        self.qty = []
        self.total = 0.00

    def update_purchases(self):
        pcode = self.ids.code_inp.text
        products_container = self.ids.products

        if pcode == '1234' or pcode == '2345':
            details = BoxLayout(size_hint_y=None, height=30, pos_hint={'top': 1})
            products_container.add_widget(details)

            code_label = Label(text=pcode, size_hint_x=.2, color=(1, 0.39, 0.28, 0.8))
            pname = "Product One" if pcode == '1234' else "Product Two"
            name = Label(text=pname, size_hint_x=.3, color=(1, 0.39, 0.28, 0.8))
            qty = Label(text='1', size_hint_x=.1, color=(1, 0.39, 0.28, 0.8))
            disc = Label(text='0.00', size_hint_x=.1, color=(1, 0.39, 0.28, 0.8))
            pprice = 1.00
            price = Label(text=str(pprice), size_hint_x=.1, color=(1, 0.39, 0.28, 0.8))
            total_price = pprice
            total = Label(text=str(total_price), size_hint_x=.2, color=(1, 0.39, 0.28, 0.8))

            details.add_widget(code_label)
            details.add_widget(name)
            details.add_widget(qty)
            details.add_widget(disc)
            details.add_widget(price)
            details.add_widget(total)

            # Update total
            self.total += pprice

            # Update preview
            self.ids.cur_product.text = pname
            self.ids.cur_price.text = str(pprice)
            preview = self.ids.receipt_preview
            prev_text = preview.text
            _prev = prev_text.find('`')
            if _prev > 0:
                prev_text = prev_text[:_prev]

            ptarget = -1
            for i, c in enumerate(self.cart):
                if c == pcode:
                    ptarget = i

            if ptarget >= 0:
                self.qty[ptarget] += 1
                expr = f'{pname}\\t\\tx\\d+'
                rexpr = f'{pname}\\t\\tx{self.qty[ptarget]}\\t'
                prev_text = re.sub(expr, rexpr, prev_text)
            else:
                self.cart.append(pcode)
                self.qty.append(1)
                prev_text += f'\n{pname}\t\tx1\t\t{pprice}'

            purchase_total = f'`\n\nTotal\t\t\t\t\t\t\t\t{self.total:.2f}'
            preview.text = prev_text + purchase_total

class OperatorApp(App):
    def build(self):
        return OperatorWindow()

if __name__ == "__main__":
    OperatorApp().run()
