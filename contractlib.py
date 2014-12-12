# WARNING!!! FULL OF PLACEHOLDERS ("")
# refactored version of https://gist.github.com/theblacksquid/3301491dd487e6a29802#file-contractlib-py
# removed repetitive ContractPart subclasses

class ContractPart:
    '''
       class ContractPart is only a base class for contract
       sub-units, not meant to be instantiated by itself.
    '''
    def __init__(self, nym, item, price, 
                 sig="", contract_exp="", party, currency="BTC"):     #param sig & sontract_exp in this 
        self.nym = nym                         #example are only placeholders
        self.item = item                       #for someone's pgp key
        self.currency = currency               #and optional expiration
        self.price = str(price)+self.currency  #therefore, "" (for now)
        self.contract_exp = contract_exp       
        self.sig = sig
        self.party = party
        self.table = {
                      "nym" : self.nym, "item" : self.item,
                      "price" : self.price, "sig" : self.sig,
                      "contract_exp" : self.contract_exp,
                      "party" : self.party
                      }

    def json_conv(self):
        result = ""
        #convert above info into JSON,
        return result

    def xml_conv(self):
        #convert above info into xml,
        #is a str obj
        result = ""
        base =   ["<%s_part>" % self.party,
                  "<party>%s</party>" % self.party,
                  "<nym>%s</nym>" % self.nym,
                  "<item>%s</item>" % self.item,
                  "<price>%s</price>" % self.price,
                  "<contract_exp>%s</contract_exp>" % self.contract_exp,
                  "<sig>%s</sig>" % self.sig,
                  "</%s_part>" % self.party]
        for item in base:
            result = result + item
        return result

    def getData(self, key):
        #gets data from above self.table; nym,
        # item, price, etc... must be in str
        return self.table[key]


class Contract():

    def __init__(self, seller_nym="", buyer_nym="",
                 notary_nym="", item="", price="",
                 sign_state="", seller_sig="",
                 buyer_sig="", notary_sig="",
                 contract_exp=""):
        #raw data
        self.seller_nym = seller_nym
        self.buyer_nym = buyer_nym
        self.notary_nym = notary_nym
        self.item = item
        self.price = price
        self.contract_exp = ""
        self.sign_state = sign_state
        self.seller_sig = seller_sig
        self.buyer_sig = buyer_sig
        self.notary_sig = notary_sig
        self.contract_hash = ""

        #initiaize ContractPart(s)
        
        #seller
        self.seller = ContractPart(self.seller_nym, self.item,
                                   self.price, self.seller_sig,
                                   self.contract_exp, "SELLER")
        #buyer
        self.buyer = ContractPart(self.buyer_nym, self.item,
                                  self.price, self.buyer_sig,
                                  self.contract_exp, "BUYER")
        #notary
        self.notary = ContractPart(self.notary_nym, self.item,
                                   self.price, self.notary_sig,
                                   self.contract_exp, "NOTARY")

        #get contract's transacting currency
        self.coin = self.seller.currency
        
    def getXML(self):
        #get separate XML objects
        seller_part = self.seller.xml_conv()
        buyer_part = self.buyer.xml_conv()
        notary_part = self.notary.xml_conv()
        #initialize containers
        result = ""
        base = [seller_part, buyer_part, notary_part]
        wrappers = {
                    "xml_head" : "<root>",
                    "xml_foot" : "</root>"
                    }
        #manipulate data
        result = result + wrappers["xml_head"]
        for item in base:
            if "<nym></nym>" in item:
                pass
            else:
                result = result + item
        result = result + wrappers["xml_foot"]
        return result   #We have to add how to add self.contract_hash
                        #when its changes every time info is added/changed
