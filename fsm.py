from transitions.extensions import GraphMachine

flag=0

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == '心好累'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == '我也喜歡玖壹壹'

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == '看三小'

    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == '是又怎樣'

    def is_going_to_state5(self, update):
        text = update.message.text
        if text.lower() == '我工程師，體諒下' :
            global flag
            flag=1
            return 1
        else :
            return 1
    def on_enter_state1(self, update):
        update.message.reply_text("弟怎了，私")
        self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state3(self, update):
        update.message.reply_text("你現在是在挑釁?")
        

    def on_exit_state3(self, update):
        print('Leaving state3')

    def on_enter_state4(self, update):
        update.message.reply_text("幹出來挑")
        

    def on_exit_state4(self, update):
        print('Leaving state4')

    def on_enter_state5(self, update):
        global flag
        if flag==1:
            self.go_back(update)
            flag=0
        else :
            update.message.reply_text("諒你不敢啦孬種")
        

    def on_exit_state5(self, update):
        print('Leaving state5')

    def on_enter_state2(self, update):
        update.message.reply_text("品味不錯兄弟\n這首-> https://www.youtube.com/watch?v=JvkqZrYJUe8")
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')
