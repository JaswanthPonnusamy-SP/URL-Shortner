


class decode_url():

    def decode(self,url):

        url_1=url[3:]

        url_2=int(url_1[:-2])

        url_3=(url_2+13)/10
        print(url_3)
        return url_3

