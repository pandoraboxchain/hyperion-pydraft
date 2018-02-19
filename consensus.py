gossip_signer_permission_size = 100

class Block:

    def __init__(self, bid, creator, time_period, transactions=[], blocked_transactions=[]):
        self.bid = bid
        self.creator = creator
        self.time_period = time_period
        self.transactions = transactions
        self.blocked_transactions = blocked_transactions

class GenesisBlock(Block):
    pass

class Gossip:

    def __init__(self, time_period, signers):
        self.time_period = time_period
        self.signers = signers

class GossipWithBlock:

    def __init__(self, time_period, signers, block):
        self.time_period = time_period
        self.signers = signers
		self.block = block

class Chain:

    def __init__(self, blocks=[]):
        self.blocks = blocks
        self.active = True

    def deactivate(self, user):
        self.active = False
        return {
            "type": "unblock transaction",
            "user": user,
        }

    def get_blocks_by_period():
        #write
        return None

#blockgeneration
#blockabsence
class TimePeriod:

    def __init__(self, timenumber):
        self.timenumber = timenumber

    def is_generation_period(self):
        return self.timenumber % 2 == 0

    def is_absence_period(self):
        return self.timenumber % 2 == 1

    def next_period(self):
        return TimePeriod(self.timenumber + 1)

	def past_period(self):
		return TimePeriod(self.timenumber + 1)

class User:

    def __init__(self, uid):
        self.uid = uid

class Permission:

    def __init__(self, user):
        self.user = user

class GenerationBlockPermission(Permission):
    pass

class AbsenceBlockPermission(Permission):
    pass

class InvalidPeriod(Exception):
    pass

class InvalidLevel(Exception):
    pass

class InvalidPermissionsSize(Exception):
    pass

class UserPermissions:

    def __init__(self):
        self.__time_period_permissions__ = {}

    def add_generation_block_permissions(self, time_period, permission):
        if not time_period.is_generation_period():
            raise InvalidPeriod("Invalid period")

        self.__time_period_permissions__[time_period.timenumber] = permission

    def add_absence_block_permissions(self, time_period, permissions):

        if not time_period.is_absence_period():
            raise InvalidPeriod("Invalid period")

        if not level in levels:
            raise InvalidLevel("Invalid level")

        if len(permissions) != gossip_signer_permission_size:
            raise InvalidLevel("Invalid permissions size")

        self.__time_period_permissions__[time_period.timenumber] = permissions

    def get_generation_block_permission(self, time_period):

        if not time_period.is_generation_period():
            raise InvalidPeriod("Invalid period")

        return self.__time_period_permissions__[time_period.timenumber]

    def get_absence_block_permissions(self, time_period):

        if not time_period.is_absence_period():
            raise InvalidPeriod("Invalid period")

        res = []
        for item in self.__time_period_permissions__[time_period.timenumber].keys():
            res = res + self.__time_period_permissions__[time_period.timenumber][item]

        return res

bid_last_id = 0
def new_bid():
    global bid_last_id
    bid_last_id = bid_last_id + 1
    return bid_last_id

class Consensus():

    def set_user_permissions(self, user_permissions):
        self.user_permissions = user_permissions

    def set_user(self, user):
        self.user = user

    def init_chain(self):
        self.chain = Chain([GenesisBlock()])
        self.time_period = TimePeriod(1)

    def __block_sign__(self):
        gb = self.user_permissions.get_generation_block_permission(self.time_period)
        if cp.user.uid == self.user.uid:
            nb = Block(new_bid(), self.user, self.time_period)
            self.chain.append(nb)
        #TO-DO describe blocked_transactions

    def __gossip_sign__(self):
        abp = self.user_permissions.get_absence_block_permissions(self.time_period)
        uids = [item.uid for item in abp]
        if cp.user.uid in uids:
            ng = Gossip(self.time_periodm, [self.user])
            self.chain.append(ng)
        #TO-DO other signers

	def sign_by_period(self):
        period = self.time_period

        if period.time_period.is_absence_period():
            if chain.get_blocks_by_period(period.past_period())==None:
                self.__gossip_sign__()
			else:
				self.__gossip_with_block_sign__()
        if period.time_period.is_generation_period():
            self.__block_sign__()

    def next_period(self):
        new = self.time_period.next_period()
        self.time_period = new

    def compare_chain(self, chain):
        if self.chain in self.chain
        #gossip priority
        #signer block priority
        #block count priority
        #tx count priority

        #merge

        #deactivate

        #send block trans
