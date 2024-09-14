from flet import *
import sqlite3

def main(page: Page):
    global theme_mode
    page.title = "تسجيل الدخول"
    page.window.height = 740
    page.window.width = 390
    page.window.top = 10
    page.window.left = 960
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    page.appbar = AppBar(
        bgcolor = colors.BLUE,
        title = Text("تسجيل الدخول"),
        center_title = True,
        leading = Icon(icons.HOME, tooltip = "الرئيسية"),
        leading_width = 40,
        actions = [
            IconButton(icons.NOTIFICATIONS, tooltip = "الاشعارات"),
            PopupMenuButton(
                items = [
                    PopupMenuItem(text = "الملف الشخصي"),
                    PopupMenuItem(text = "اعدادات التطبيق"),
                    PopupMenuItem(text = "من نحن"),
                    PopupMenuItem(),
                    PopupMenuItem(text = "اغلاق التطبيق"),
                ],
                tooltip = "المزيد"
            ),
        ],
    )

    def show(e):
        con = sqlite3.connect("db.db")
        cur = con.cursor()
        v1 = en1.value
        v2 = en2.value

        cur.execute("CREATE TABLE IF NOT EXISTS users(username STR, password STR, email STR)")
        cur.execute("INSERT INTO users(username, password, email) VALUES('hamada', '3102', 'hamda22@gmail.com')")
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
            

        alert1 = AlertDialog(
            # title = Text("Data Error: Username or Password is Wrong SignUp if you don't have Account", size = 18, color = 'red')
        )
        correct = False

        for row in rows:
            if v1 == row[2] and v2 == str(row[1]):
                alert1 = AlertDialog(
                    title = Text(f"Welcome {row[0]}", size = 18, color = 'green')
                )
                correct = True
        
        page.overlay.append(alert1)
        alert1.open = True
        page.update()

        con.commit()
        con.close()
        


    image = Image(src = "assets/icon.png", width = 170)
    text = Text("لوحة تسجيل الدخول", color = 'white')
    en1 = TextField(label = "البريد الالكتروني", icon = icons.EMAIL)
    en2 = TextField(label = "كلمة المرور", icon = icons.PASSWORD, password = True, can_reveal_password = True)
    btn1 = ElevatedButton('الدخول للحساب', on_click = show)
    link1 = Text()



    page.add(image, text, en1, en2, btn1)

    page.navigation_bar = CupertinoNavigationBar(
        bgcolor = colors.BLUE,
        inactive_color = colors.BLACK,
        active_color = colors.WHITE,
        destinations = [
            NavigationBarDestination(icon = icons.CALL, label = 'اتصال'),
            NavigationBarDestination(icon = icons.CAMERA, label = 'كاميرا'),
            NavigationBarDestination(icon = icons.CONTACT_PHONE, label = 'جهات الاتصال'),
        ]
    )

    page.update()


app(main)# -> iphone, android
# app(target = main)# -> windows
# app(target=main, assets_dir="assets", view=AppView.WEB_BROWSER)# -> wbsite with download option, also if doesn't work you can write port = #### and write any number
