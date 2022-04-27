from last_urlid import last_url


class encode_url():

    def encode(self):

        last = last_url()
        value_1 = last.lasturl()
        value_2=value_1
        multiply=(value_2*10)-13
        encodevalue="JAz"+str(multiply)+"Mc"
        print(encodevalue)

        return encodevalue

