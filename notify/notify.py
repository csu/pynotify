import abc

class Notifier(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def send(self, message, recipient=None, title=None, source=None, open_url=None):
        print 'notification:'
        print 'recipient: %s' % recipient
        print 'message: %s' % message