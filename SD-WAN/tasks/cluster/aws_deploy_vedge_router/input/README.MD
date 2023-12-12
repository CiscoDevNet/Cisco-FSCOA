https://www.cisco.com/c/en/us/td/docs/routers/sdwan/configuration/sdwan-xe-gs-book/cisco-sd-wan-overlay-network-bringup.html#c_Configure_the_vManage_NMS_8301.xml


Configuration
=====

At a minimum, you must configure the IP address of your network's Cisco vBond Orchestrator, the device's system IP address, and a tunnel interface in VPN 0 to use for exchanging control traffic among the network controller devices (the Cisco vBond Orchestrator, Cisco vManage, and Cisco vSmart Controller devices).

For the overlay network to be operational and for Cisco vManage instances to participate in the overlay network, you must do the following:

Configure a tunnel interface on at least one interface in VPN 0. This interface must connect to a WAN transport network that is accessible by all Cisco vEdge devices. VPN 0 carries all control plane traffic among the Cisco vEdge devices in the overlay network.

Ensure that the Overlay Management Protocol (OMP) is enabled. OMP is the protocol responsible for establishing and maintaining the Cisco SD-WAN control plane. OMP is enabled by default, and you cannot disable it. If you edit the configuration from the CLI, do not remove the omp configuration command.

