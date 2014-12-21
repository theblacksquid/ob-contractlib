# WARNING!!! FULL OF PLACEHOLDERS ("")
import json
from collections import OrderedDict

class ContractPart:
    '''
       class ContractPart is only a base class for contract
       sub-units, not meant to be instantiated by itself.
    '''
    def __init__(self, nym="", gpgID="", secp="",
                 hashID="",

                 item="", price="", condition="",
                 qty="", keyword="", region="",
                 est_deliv="", ship_fee="",
                 currency="BTC", item_pic="",

                 contract_exp=""):   
        self.nym = nym
        self.gpg = gpgID
        self.hashID = hashID
        self.secp = secp
        
        self.item = item                       
        self.currency = currency               
        self.price = str(price)+self.currency
        self.cond = condition
        self.qty = qty
        self.kword = keyword
        self.region = region
        self.eta = est_deliv
        self.ship = ship_fee
        self.item_pic = item_pic

        self.contract_exp = contract_exp

        # attr get is used as example.get[query]
        self.get = {
                      "item" : self.item, "price" : self.price,
                      "condition" : self.cond, "quantity" : self.qty,
                      "keywords" : self.kword, "region" : self.region,
                      "est_delivery" : self.eta,
                      "shipping fee" : self.ship,
                      "contract_exp" : self.contract_exp,
                      
                      "nym" : self.nym, "GPG" : self.gpg,
                      "secp256k1" : self.secp
                      }
# I apologize for the mess in advance
class Contract():

    def __init__(self, seller_nym="", seller_gpg="",
                 seller_secp="", seller_hashID="",

                 buyer_nym="", buyer_gpg="",
                 buyer_secp="", buyer_hashID="",

                 notary_nym="", notary_gpg="",
                 notary_secp="", notary_hashID="",

                 item="", price="", condition="",
                 item_qty="", keywords="", region="",
                 ship_fee="", eta="", coin="",
                 item_img="", 

                 contract_exp="", contract_ver="",
                 item_category="", subCategory=""):
        
        # metadata
        self.nonce = ""
        self.contract_exp = contract_exp
        self.contract_ver = contract_ver
        self.category = item_category
        self.subCategory = subCategory

        # order details
        self.item = item; self.cond = condition;
        self.price = price; self.qty = item_qty;
        self.kword = keywords; self.region = region;
        self.ship_fee = ship_fee; self.coin = coin;
        self.img = item_img; self.eta = eta
        
        # IDs and sigs from the three parties
        ####################
        # seller
        self.seller_nym = seller_nym
        self.seller_gpg = seller_gpg
        self.seller_secp = seller_secp
        self.seller_hashID = seller_hashID

        # buyer
        self.buyer_nym = buyer_nym
        self.buyer_gpg = buyer_gpg
        self.buyer_secp = buyer_secp
        self.buyer_hashID = buyer_hashID

        # notary
        self.notary_nym = notary_nym
        self.notary_gpg = notary_gpg
        self.notary_secp = notary_secp
        self.notary_hashID = notary_hashID
        
        # initiaize ContractPart(s)
        ####################
        #genesisPart
        self.genesis = ContractPart(item = self.item, 
                                    price = self.price,
                                    item_pic = self.img,
                                    condition = self.cond,
                                    qty = self.qty,
                                    keyword = self.kword,
                                    region = self.region,
                                    est_deliv = self.eta,
                                    ship_fee = self.ship_fee,
                                    contract_exp = self.contract_exp)
        #sellerPart
        self.seller = ContractPart(nym = self.seller_nym,
                                   gpgID = self.seller_gpg,
                                   secp = self.seller_secp,
                                   hashID = self.seller_hashID,)
        #buyerPart
        self.buyer = ContractPart(nym = self.buyer_nym,
                                  gpgID = self.buyer_gpg,
                                  secp = self.buyer_secp,
                                  hashID = self.buyer_hashID,)
        #notaryPart
        self.notary = ContractPart(nym = self.notary_nym,
                                   gpgID = self.notary_gpg,
                                   secp = self.notary_secp,
                                   hashID = self.notary_hashID,)
        self.genPart = {
                "GenesisPart" : {
                    
                    "metadata" : {
                        "OBCv" : "%s" % self.contract_ver,
                        "Category" : "%s" % self.category,
                        "subCategory" : "%s" % self.subCategory,
                        "Expiration_Date" : "%s" % self.contract_exp
                        },
                    
                    "nonce" : "", # Wouldn't it be a good idea to keep a
                                  # chain of nonces to track the history of changes
                                  # to the current contract?                     
                    "item_data" : {
                        "item_title" : "%s" % self.item,
                        "%s_price" % self.coin : "0.00 %s" % self.coin,
                        "fiat_price" : "", ##
                        # Are we going to use a
                        # standard API for getting fiat prices?
                        "item_image" : "%s" % self.img,
                        "item_condition" : "%s" % self.cond,
                        "quantity" : "%s" % self.qty,
                        "keywords" : "%s" % self.kword,
                        "region" : "%s" % self.region,
                        "est_delivery" : "%s" % self.eta,
                        "shipping_fee" : "%s" % self.ship_fee
                        }
                    }
                }
        self.sellerPart = {
            "MerchantPart" : {
                "Merchant_ID" : "%s" % self.seller_nym,
                "signatures" : {
                    "Hash" : "%s" % self.seller_hashID,
                    "GPG" : "%s" % self.seller_gpg,
                    "secp256k1" : "%s" % self.seller_secp
                    }
                }
            }
            
                
        self.buyerPart = {
            "BuyerPart" : {
                "Buyer_ID" : "%s" % self.buyer_nym,
                "signatures" : {
                    "Hash" : "%s" % self.buyer_hashID,
                    "GPG" : "%s" % self.buyer_gpg,
                    "secp256k1" : "%s" % self.buyer_secp
                    }
                }
            }
            
        self.notaryPart = {
            "NotaryPart" : {
                "Notary_ID" : "%s" % self.notary_nym,
                "signatures" : {
                    "Hash" : "%s" % self.notary_hashID,
                    "GPG" : "%s" % self.notary_gpg,
                    "secp256k1" : "%s" % self.notary_secp
                    }
                }
            }
                                   
    def getJSON(self):
        # initialize containers
        contract = OrderedDict()
        gPart = self.genPart["GenesisPart"]
        sPart = self.sellerPart["MerchantPart"]
        bPart = self.buyerPart["BuyerPart"]
        nPart = self.notaryPart["NotaryPart"]
        result = None

        # produce the contact depending on who has signed and not
        # good for several use cases; note that these are
        # made under the assumption that a notary will only be
        # involved once both seller and buyer are present
        contract["GenesisPart"] = gPart
        
        # standard "I list an item I want to sell"
        if self.buyerPart["BuyerPart"]["Buyer_ID"] == "":
            contract["MerchantPart"] = sPart
            result = json.dumps(contract)
            return result
        # "This is something I want to buy at yea price"
        elif self.sellerPart["MerchantPart"]["Merchant_ID"] == "":
            contract["BuyerPart"] = bPart
            result = json.dumps(contract)
            return result
        # triple signed contract
        else:
            contract["MerchantPart"] = sPart
            contract["BuyerPart"] = bPart
            result = json.dumps(contract)
            return result

