# Strings / localization file for greed
# Can be edited, but DON'T REMOVE THE REPLACEMENT FIELDS (words surrounded by {curly braces})

# Currency symbol
currency_symbol = "$"

# Positioning of the currency symbol
currency_format_string = "{symbol} {value}"

# Quantity of a product in stock
in_stock_format_string = "{quantity} متوفـر"

# Copies of a product in cart
in_cart_format_string = "{quantity} في السـلة"

# Product information
product_format_string = "<b>{name}</b>\n" \
                        "{description}\n" \
                        "{price}\n" \
                        "<b>{cart}</b>"

# Order number, displayed in the order info
order_number = "الطلـب #{id}"

# Order info string, shown to the admins
order_format_string = "by {user}\n" \
                      "تاريخ الطلب {date}\n" \
                      "\n" \
                      "{items}\n" \
                      "المجموع: <b>{value}</b>\n" \
                      "\n" \
                      "ملاحظات الزبون : {notes}\n"

# Order info string, shown to the user
user_order_format_string = "{status_emoji} <b>الطلب {status_text}</b>\n" \
                           "{items}\n" \
                           "المجموع : <b>{value}</b>\n" \
                           "\n" \
                           "الملاحظات : {notes}\n"

# Transaction page is loading
loading_transactions = "<i>تحميل المعاملات ...\n" \
                       "الرجاء الانتظار بضع ثوان.</i>"

# Transactions page
transactions_page = "صفحة <b>{page}</b>:\n" \
                    "\n" \
                    "{transactions}"

# transactions.csv caption
csv_caption = "A 📄 .csv تم إنشاء ملف يحتوي على جميع المعاملات المخزنة في قاعدة بيانات الروبوت.\n" \
              "يمكنك فتح هذا الملف باستخدام برامج أخرى، مثل LibreOffice Calc، لمعالجته" \
              " البيانات."

# Conversation: the start command was sent and the bot should welcome the user
conversation_after_start = "مرحباً!\n" \
                           "مرحباً بك في متجري!\n" \
                           "This is the 🅱️ <b>Beta</b> version of the software.\n" \
                           "It is fully usable, but there may be some bugs are still present.\n" \
                           "If you find any, please report them at https://github.com/Steffo99/greed/issues."

# Conversation: to send an inline keyboard you need to send a message with it
conversation_open_user_menu = "ماذا ترغب ان تفعل؟\n" \
                              "💰 لديك <b>{credit}</b> في محفظتك.\n" \
                              "\n" \
                              "<i>اضغط على مفتاح القائمة في لوحة المفاتيح السفلية لتحديد عملية.\n" \
                              "إذا لم يتم فتح لوحة المفاتيح، يمكنك فتحها بالضغط على الزر بأربعة أزرار صغيرة" \
                              " المربعات في شريط الرسائل.</i>"

# Conversation: like above, but for administrators
conversation_open_admin_menu = "أنت 💼 <b>المدير</b> لهذا المتجر!\n" \
                               "ماذا تريد أن تفعل؟\n" \
                               "\n" \
                               "<i>اضغط على مفتاح القائمة في لوحة المفاتيح السفلية لتحديد عملية.\n" \
                               "إذا لم يتم فتح لوحة المفاتيح، فيمكنك فتحها بالضغط على الزر ذو المربعات الصغيرة الأربعة." \
                               " في شريط الرسائل.</i>"

# Conversation: select a payment method
conversation_payment_method = "كيف تريد إضافة الأموال إلى محفظتك؟"

# Conversation: select a product to edit
conversation_admin_select_product = "✏️ ما هو المنتج الذي تريد تعديله؟"

# Conversation: select a product to delete
conversation_admin_select_product_to_delete = "❌ ما هو المنتج الذي تريد حذفه؟"

# Conversation: select a category to edit
conversation_admin_select_category = "✏️ ما هي الفئة التي تريد تحريرها؟"

# Conversation: select a category to delete
conversation_admin_select_category_to_delete = "❌ ما الفئة التي تريد حذفها؟"

# Conversation: select a user to edit
conversation_admin_select_user = "👥 حدد المستخدم لتحريره."

# Conversation: click below to pay for the purchase
conversation_cart_actions = "<i> أضف المنتجات إلى سلة التسوق من خلال التمرير لأعلى والضغط على زر الإضافة أسفل" \
                            " المنتجات التي تريد إضافتها إلى سلة التسوق. عند الانتهاء، ارجع إلى هذه الرسالة و" \
                            " اضغط على زر تم أدناه.</i>"

# Conversation: select category
conversation_select_category = "اختر فئة"

# Conversation: confirm the cart contents
conversation_confirm_cart = "🛒 تحتوي سلة التسوق الخاصة بك على المنتجات التالية:\n" \
                            "{product_list}" \
                            "المجموع: <b>{total_cost}</b>\n" \
                            "\n" \
                            "<i>إذا كنت تريد المتابعة، اضغط على زر تم الموجود أسفل هذه الرسالة. .\n" \
                            "للإلغاء، اضغط على زر إلغاء.</i>"

# Live orders mode: start
conversation_live_orders_start = "أنت في وضع <b>الطلبات المباشرة</b>.\n" \
                                 "ستظهر جميع الطلبات الجديدة التي يقدمها العملاء في الوقت الفعلي في هذه الدردشة،" \
                                 " وستتمكن من وضع علامة عليها بأنها ✅ مكتملة" \
                                 " أو ✴️ إعادة الرصيد للعميل."

# Live orders mode: stop receiving messages
conversation_live_orders_stop = "<i>اضغط على زر الإيقاف الموجود أسفل هذه الرسالة لإيقاف" \
                                " البث.</i>"

# Conversation: help menu has been opened
conversation_open_help_menu = "ما هو نوع المساعدة التي تحتاجها؟"

# Conversation: confirm promotion to admin
conversation_confirm_admin_promotion = "هل أنت متأكد من أنك تريد ترقية هذا المستخدم إلى 💼 مدير?\n" \
                                       "هذا إجراء لا رجعة فيه!"

# Conversation: language select menu header
conversation_language_select = "اختر لغة:"

# Conversation: switching to user mode
conversation_switch_to_user_mode = " أنت تقوم بالتبديل إلى 👤 وضع العميل.\n" \
                                   "إذا كنت تريد العودة إلى 💼 قائمة مدير, فأعد تشغيل المحادثة باستخدام /start."

# Notification: the conversation has expired
conversation_expired = "🕐  لم أتلق أي رسائل منذ فترة، لذا قمت بإغلاق المحادثة لتوفير " \
                       " الموارد/الوقت.\n" \
                       "إذا كنت تريد بدء أمر جديد, أرسل الأمر /start من جديد."

# Menu: all products
menu_all_products = "جميع المنتجات"

# Menu: uncategorized
menu_uncategorized = "غير مصنف"

# User menu: order
menu_order = "🛒 اطلب منتجات"

# User menu: order status
menu_order_status = "🛍 طلباتي"

# User menu: add credit
menu_add_credit = "💵 إضافة أموال"

# User menu: bot info
menu_bot_info = "ℹ️ معلومات عن البوت"

# User menu: cash
menu_cash = "💵 With cash"

# User menu: credit card
menu_credit_card = "💳 By credit card"

# Admin menu: products
menu_products = "📝️ المنتجات"

# Admin menu: categories
menu_categories = "📝️ فئات"

# Admin menu: orders
menu_orders = "📦 الطلبات"

# Menu: transactions
menu_transactions = "💳 قائمة المعاملات"

# Menu: edit credit
menu_edit_credit = "💰 إنشاء معاملة"

# Admin menu: go to user mode
menu_user_mode = "👤 التبديل إلى وضع العميل"

# Admin menu: add product
menu_add_product = "✨ إنشاء منتج جديد"

# Admin menu: delete product
menu_delete_product = "❌ حذف منتج موجود"

# Admin menu: add category
menu_add_category = "✨ إنشاء فئة جديدة"

# Admin menu: delete category
menu_delete_category = "❌ حذف فئة موجودة"

# Menu: cancel
menu_cancel = "🔙 الرجوع"

# Menu: go back
menu_go_back = "🔙 Go back"

# Menu: skip
menu_skip = "⏭ تخطي"

# Menu: done
menu_done = "✅️ تم"

# Menu: pay invoice
menu_pay = "💳 دفع"

# Menu: complete
menu_complete = "✅ Complete"

# Menu: refund
menu_refund = "✴️ إعادة"

# Menu: stop
menu_stop = "🛑 توقف"

# Menu: add to cart
menu_add_to_cart = "➕ إضافة"

# Menu: remove from cart
menu_remove_from_cart = "➖ إزالة"

# Menu: select the size
menu_add_size = ["S", "M", "L", "XL"]

# Menu: select the color
menu_add_color = ["White", "Black", "Gray", "Red","Blue"]

# Menu: help menu
menu_help = "❓ المساعدة / الدعم"

# Menu: guide
menu_guide = "📖 دليل الاستخدام"

# Menu: next page
menu_next = "▶️ التالي"

# Menu: previous page
menu_previous = "◀️ السابق"

# Menu: contact the shopkeeper
menu_contact_shopkeeper = "👨‍💼 تواصل مع المتجر"

# Menu: generate transactions .csv file
menu_csv = "📄 .csv"

# Menu: edit admins list
menu_edit_admins = "🏵 تعديل المدراء"

# Menu: language
menu_language = "🇸🇦 اللغة"

# Emoji: unprocessed order
emoji_not_processed = "*️⃣"

# Emoji: completed order
emoji_completed = "✅"

# Emoji: refunded order
emoji_refunded = "✴️"

# Emoji: yes
emoji_yes = "✅"

# Emoji: no
emoji_no = "🚫"

# Text: unprocessed order
text_not_processed = "قيد الانتظار"

# Text: completed order
text_completed = "مكتمل"

# Text: refunded order
text_refunded = "تم استرداد المبلغ/مسترجع"

# Add product: category?
ask_product_category = "ماذا يجب أن تكون فئة المنتج؟"

# Add product: name?
ask_product_name = "ماذا يجب أن يكون اسم المنتج؟"

# Add product: description?
ask_product_description = "ماذا ينبغي أن يكون وصف المنتج؟"

# Add product: size?
ask_product_size = "ما هي القياسات المتوفرة؟"

# Add product: color?
ask_product_color = "ما هي ألوان المنتج المتوفرة؟ "

# Add product: price?
ask_product_price = "ما هو السعر الذي يجب أن يكون عليه المنتج؟?\n" \
                    "أدخل <code>X</code> إذا كنت لا تريد أن يكون المنتج معروضًا للبيع بعد."

# Add product: Not for sale yet (Non in vendita) text
not_for_sale_yet = "ليس متاحاً للبيع بعد"

# Add product: image?
ask_product_image = "🖼 ما هي الصورة التي تريد أن يكون عليها المنتج؟\n" \
                    "\n" \
                    "<i>أرسل الصورة، أو تخطى هذه المرحلة ولا تقم بإضافة أي صورة.</i>"

# Add category: name?
ask_category_name = "ماذا ينبغي أن يكون اسم الفئة؟"

# Order product: notes?
ask_order_notes = "هل ترغب في ترك ملاحظة مع الطلب؟\n" \
                  "💼 ستكون مرئية لمديري المتجر.\n" \
                  "\n" \
                  "<i>أرسل رسالة بالملاحظة التي تريد تركها، أو اضغط على زر التخطي أسفل هذه" \
                  " الرسالة لتركها فارغة.</i>"

# Refund product: reason?
ask_refund_reason = " قم بإرفاق سبب لرفض الطلب.\n" \
                    "👤  سيكون ظاهراً للعميل."

# Edit credit: notes?
ask_transaction_notes = " قم بإرفاق ملاحظة لهذه المعاملة.\n" \
                        "👤 سوف تكون مرئية للعميل بعد الإيداع / الخصم" \
                        " وإلى 💼 المسؤولين في سجل المعاملات."

# Edit credit: amount?
ask_credit = "كيف تريد تغيير رصيد العميل؟\n" \
             "\n" \
             "<i>أرسل رسالة تحتوي على المبلغ.\n" \
             "استخدم العلامة </i><code>+</code><i> لإضافة رصيد إلى حساب العميل،" \
             " والعلامة </i><code>-</code><i> لخصم الرصيد.</i>"

# Header for the edit admin message
admin_properties = "<b>صلاحيات  {name}:</b>"

# Edit admin: can edit products?
prop_edit_products = "تعديل المنتجات"

# Edit admin: can edit categories?
prop_edit_categories = "تحرير الفئات"

# Edit admin: can receive orders?
prop_receive_orders = "تلقي الطلبات"

# Edit admin: can create transactions?
prop_create_transactions = "إدارة المعاملات"

# Edit admin: show on help message?
prop_display_on_help = "عرض للعميل "

# Thread has started downloading an image and might be unresponsive
downloading_image = "أقوم بتحميل صورتك!\n" \
                    "ربما يستغرق الأمر بعض الوقت... يرجى التحلي بالصبر!\n" \
                    "لن أتمكن من الرد عليك أثناء قيامي بالتحميل."

# Edit product: current value
edit_current_value = "القيمة الحالية هي:\n" \
                     "<pre>{value}</pre>\n" \
                     "\n" \
                     "<i>اضغط على زر التخطي الموجود أسفل هذه الرسالة للاحتفاظ بنفس القيمة.</i>"

# Payment: cash payment info
payment_cash = "يمكنك الدفع نقدًا في الموقع الفعلي للمتجر.\n" \
               "ادفع عند الخروج، وأعطي هذا المعرف للمدير:\n" \
               "<b>{user_cash_id}</b>"

# Payment: invoice amount
payment_cc_amount = "كم من الأموال تريد إضافتها إلى محفظتك؟\n" \
                    "\n" \
                    "<i>حدد مبلغًا باستخدام الأزرار أدناه، أو أدخله يدويًا باستخدام لوحة المفاتيح العادية</i>"

# Payment: add funds invoice title
payment_invoice_title = "إضافة الأموال"

# Payment: add funds invoice description
payment_invoice_description = "سيؤدي دفع هذه الفاتورة إلى إضافة {amount} إلى محفظتك."

# Payment: label of the labeled price on the invoice
payment_invoice_label = "إعادة تحميل"

# Payment: label of the labeled price on the invoice
payment_invoice_fee_label = "رسوم التحويل"

# Notification: order has been placed
notification_order_placed = "تمت إضافة طلب جديد:\n" \
                            "\n" \
                            "{order}"

# Notification: order has been completed
notification_order_completed = "لقد تم إكمال طلبك!\n" \
                               "\n" \
                               "{order}"

# Notification: order has been refunded
notification_order_refunded = "لقد تم الغاء طلبك واسترداد أموالك!\n" \
                              "\n" \
                              "{order}"

# Notification: a manual transaction was applied
notification_transaction_created = "ℹ️  لقد تم تطبيق معاملة جديدة على محفظتك:\n" \
                                   "{transaction}"

# Refund reason
refund_reason = "سبب الاسترداد:\n" \
                "{reason}"

# Info: informazioni sul bot
bot_info = 'This bot is using <a href="https://github.com/Steffo99/greed">greed</a>,' \
           ' a framework by @Steffo for Telegram payments released under the' \
           ' <a href="https://github.com/Steffo99/greed/blob/master/LICENSE.txt">' \
           'Affero General Public License 3.0</a>.\n'

# Help: guide
help_msg = "greed's guide is available at this address:\n" \
           "https://github.com/Steffo99/greed/wiki"

# Help: contact shopkeeper
contact_shopkeeper = "حاليًا، يتكون فريق الموظفين المتاحين لتقديم المساعدة للمستخدمين من:\n" \
                     "{shopkeepers}\n" \
                     "<i>انقر / اضغط على أحد أسمائهم للتواصل معهم في دردشة تليجرام</i>"

# Success: product has been added/edited to the database
success_product_edited = "✅ لقد تمت إضافة المنتج/تعديله بنجاح!"

# Success: product has been added/edited to the database
success_product_deleted = "✅ تم حذف المنتج بنجاح!"

# Success: category has been added/edited to the database
success_category_edited = "✅ تمت إضافة/تعديل الفئة بنجاح!"

# Success: category has been added/edited to the database
success_category_deleted = "✅ تم حذف الفئة بنجاح!"

# Success: order has been created
success_order_created = "✅ تم إرسال الطلب بنجاح!\n" \
                        "\n" \
                        "{order}"

# Success: order was marked as completed
success_order_completed = "✅ لقد قمت بوضع علامة على الطلب #{order_id} as completed."

# Success: order was refunded successfully
success_order_refunded = "✴️ الطلب #{order_id} مسترد."

# Success: transaction was created successfully
success_transaction_created = "✅ تم إنشاء المعاملة بنجاح!\n" \
                              "{transaction}"

# Error: message received not in a private chat
error_nonprivate_chat = "⚠️ هذا البوت يعمل فقط في الدردشات الخاصة."

# Error: a message was sent in a chat, but no worker exists for that chat.
# Suggest the creation of a new worker with /start
error_no_worker_for_chat = "⚠️ تم قطع المحادثة مع البوت.\n" \
                           " لإعادة تشغيلها، أرسل الأمر /start إلى البوت."

# Error: a message was sent in a chat, but the worker for that chat is not ready.
error_worker_not_ready = "🕒 المحادثة مع البوت قيد البدء حاليًا!.\n" \
                         "يرجى الانتظار لبضع لحظات قبل إرسال المزيد من الأوامر!"

# Error: add funds amount over max
error_payment_amount_over_max = "⚠️ الحد الأقصى للمبلغ الذي يمكن إضافته في معاملة واحدة هو {max_amount}."

# Error: add funds amount under min
error_payment_amount_under_min = "⚠️ الحد الأدنى للمبلغ الذي يمكن إضافته في معاملة واحدة هو {min_amount}."

# Error: the invoice has expired and can't be paid
error_invoice_expired = "⚠️ انتهت صلاحية هذه الفاتورة وتم إلغاؤها. إذا كنت لا تزال ترغب في إضافة أموال، فاستخدم إضافة" \
                        " خيار قائمة الأموال."

# Error: a product with that name already exists
error_duplicate_name = "️⚠️ يوجد منتج يحمل نفس الاسم بالفعل."

# Error: not enough credit to order
error_not_enough_credit = "⚠️ ليس لديك رصيد كافي لتقديم الطلب."

# Error: order has already been cleared
error_order_already_cleared = "⚠️  لقد تمت معالجة هذا الطلب بالفعل."

# Error: no orders have been placed, so none can be shown
error_no_orders = "⚠️  لم تقم بوضع أي طلب بعد، لذا لا يوجد شيء لعرضه."

# Error: selected user does not exist
error_user_does_not_exist = "⚠️  المستخدم المحدد غير موجود."

# Fatal: conversation raised an exception
fatal_conversation_exception = "☢️ أوه لا! حدث <b>خطأ</b> ما أدى إلى مقاطعة هذه المحادثة.\n" \
                               "تم الإبلاغ عن الخطأ إلى مالك الروبوت حتى يتمكن من إصلاحه.\n" \
                               "لإعادة تشغيل المحادثة، أرسل الأمر /start مرة أخرى."
