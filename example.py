digraph G {
    node [shape=ellipse, fontname="Arial", fontsize=10, style=filled, color=lightgray];
    edge [color=black, penwidth=2];
    
    subgraph cluster_1 {
        label="Perimeter Security";
        node [color=yellow, fillcolor=lightyellow];
        Firewall;
        IDS [label="Intrusion\nDetection\nSystem"];
        IPS [label="Intrusion\nPrevention\nSystem"];
        LoadBalancer;
        SSL;
        {rank=same; Firewall; IDS; IPS; LoadBalancer; SSL;}
    }
    
    subgraph cluster_2 {
        label="Network Security";
        node [color=blue, fillcolor=lightblue];
        Router;
        Switch;
        WirelessAP [label="Wireless AP"];
        VPN;
        {rank=same; Router; Switch; WirelessAP; VPN;}
    }
    
    subgraph cluster_3 {
        label="Endpoint Security";
        node [color=green, fillcolor=palegreen];
        Antivirus;
        HostIPS [label="Host-based\nIntrusion\nPrevention\nSystem"];
        Patching;
        Encryption;
        {rank=same; Antivirus; HostIPS; Patching; Encryption;}
    }
    
    subgraph cluster_4 {
        label="Application Security";
        node [color=red, fillcolor=pink];
        WAF [label="Web\nApplication\nFirewall"];
        Database;
        Encryption;
        {rank=same; WAF; Database; Encryption;}
    }
    
    subgraph cluster_5 {
        label="Social Engineering Prevention";
        node [color=orange, fillcolor=lightcoral];
        EmployeeTraining [label="Employee\nTraining"];
        PhishingProtection [label="Phishing\nProtection\nService"];
        {rank=same; EmployeeTraining; PhishingProtection;}
    }
    
    subgraph cluster_6 {
        label="Incident Response";
        node [color=purple, fillcolor=lavender];
        SIEM [label="Security\nInformation\nand Event\nManagement"];
        Forensics;
        Remediation;
        {rank=same; SIEM; Forensics; Remediation;}
    }
    
    {rank=same; Firewall; Router; Antivirus; WAF; EmployeeTraining; SIEM;}
    Firewall -> IDS;
    IDS -> IPS;
    Router -> Switch;
    Router -> LoadBalancer;
    Switch -> WirelessAP;
    WirelessAP -> HostIPS;
    VPN -> Firewall;
    WAF -> Database;
    Database -> Encryption;
    EmployeeTraining -> PhishingProtection;
    SIEM -> Forensics;
    Forensics -> Remediation;
}
