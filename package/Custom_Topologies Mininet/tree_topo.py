from mininet.topo import Topo

class MyTreeTopo(Topo):
    def _init_(self, depth=2, fanout=2, **opts):
        # Initialize topology and default options
        super(MyTreeTopo, self)._init_(**opts)
        
        # Add hosts and switches
        self.hostNum = 1
        self.switchNum = 1
        self.addTree(depth, fanout)
    
    def addTree(self, depth, fanout):
        # Create root switch
        self.addSwitch('s1')

        # Create child switches recursively
        self.addTreeHelper(1, depth, fanout)
    
    def addTreeHelper(self, current_depth, depth, fanout):
        if current_depth > depth:
            return
        
        # Add fanout child switches
        for i in range(fanout):
            # Create switch
            switch_name = 's{}'.format(self.switchNum)
            self.addSwitch(switch_name)
            self.switchNum += 1

            # Connect switch to parent switch
            parent_switch = 's{}'.format(self.switchNum // fanout)
            self.addLink(parent_switch, switch_name)

            # Recursively add child switches
            self.addTreeHelper(current_depth + 1, depth, fanout)

            # Add hosts to switch
            for j in range(fanout):
                host_name = 'h{}'.format(self.hostNum)
                self.addHost(host_name)
                self.addLink(switch_name, host_name)
                self.hostNum += 1

topo = MyTreeTopo(depth=2, fanout=3)