from twisted.cred.checkers import AllowAnonymousAccess, InMemoryUsernamePasswordDatabaseDontUse
from twisted.cred.portal import Portal
from twisted.internet import reactor
from twisted.protocols.ftp import FTPFactory, FTPRealm

checker = InMemoryUsernamePasswordDatabaseDontUse()
checker.addUser('test', "123456")
checker.addUser('someuser', "123456")
checker.addUser('anotheruser', "password")

portal = Portal(FTPRealm("./public", "/myusers"), [AllowAnonymousAccess()])

factory = FTPFactory(portal)

reactor.listenTCP(21, factory)
reactor.run()