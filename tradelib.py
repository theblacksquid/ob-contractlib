# WARNING!!! : Work-in-Prograss, full of placeholders

import contractlib

class Trade:
    
    def __init__(self, contractObj):

        # load the contract details
        self.contract = contractObj

        # order details
        self.item = contractObj.item
        self.price = contractObj.price
        self.currency = contractObj.coin

        # nyms
        self.seller_nym = contractObj.seller.nym
        self.buyer_nym = contractObj.buyer.nym
        self.notary_nym = contractObj.seller.nym

        # sigs
        self.seller_sig = contractObj.seller.sig
        self.buyer_sig = contractObj.buyer.sig
        self.notary_sig = contractObj.notary.sig

        # contract metadata
        self.exp = contractObj.contract_exp
        self.state = contractObj.sign_state
        self.hash = contractObj.contract_hash
        

    def update_hash(self):
        # update the contract hash at 
        # the foot of the contract
        pass

    def changeState(self):
        """
        changes the contract state into (but not limited to) 
        any of the given :
        
        *NO-SIGN - The contract does not have 
                   any of the partcipants' sigs

        *SIGNED - The contract has been signed by the 
                  seller's sig.

        *DOUBLE-SIGNED - Contract has been signed by both 
                         Seller and Buyer.

        *TRIPLE-SIGNED/INIT - Contract has been signed by 
                              all parties, no shipping conf yet

        *TRIPLE-SIGNED/CONF - Contract has been signed by all
                              parties, shipping confirmed, 
                              payment released to seller

        *TRIPLE-SIGNED/DISP - Contract signed by all parties
                              Item under dispute

        *TRIPLE-SIGNED/F.REF - Signed by all parties. Full refund
                               sent to buyer

        *TRIPLE-SIGNED/P.REF - Signed by all parties. Partial 
                               refund sent to buyer
        """
        pass
