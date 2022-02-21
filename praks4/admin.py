from praks3.kasutaja import Kasutaja
class Admin(Kasutaja):
    privileegid = []

    def naita_privileegid(self):
        for i in self.privileegid:
            print(i)