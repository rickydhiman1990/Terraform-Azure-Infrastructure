rg = {

  rg1 = {

    name     = "princerg1"
    location = "centralindia"

  }

  rg2 = {

    name     = "princerg2"
    location = "centralindia"

  }

    rg3 = {

    name     = "princerg3"
    location = "centralindia"
    }
    
    rg4 = {

    name     = "princerg4"
    location = "centralindia"
    #new rg 4 added here 

  }
  rg5 = {

    name     = "princerg5"
    location = "centralindia"
    #new rg 5 added here 

  }
}

vnet = {

  vnet1 = {

    name                = "hubvnet"
    location            = "centralindia"
    resource_group_name = "princerg1"
    address_space       = ["10.0.0.0/16"]
  }
}

subnet = {

  subnet1 = {

    name                 = "hubsub"
    resource_group_name  = "princerg1"
    virtual_network_name = "hubvnet"
    address_prefixes     = ["10.0.1.0/24"]
  }
}

pip = {

  pip1 = {

    name                = "frontpip"
    resource_group_name = "princerg1"
    location            = "centralindia"
    allocation_method   = "Static"
  }
}



nic = {

  nic1 = {

    nic_name        = "testnic1"
    nic_location    = "centralindia"
    nic_rg          = "princerg1"
    nic_subnet_name = "hubsub"
    nic_pip_name    = "frontpip"
    nic_vnet_name   = "hubvnet"




  }
}


vm = {

  machine1 = {

    vm_nicname             = "testnic1"
    vm_name                = "defender1"
    vm_location            = "centralindia"
    vm_resource_group_name = "princerg1"
    vm_size                = "Standard_D2s_v3"
    vm_publisher           = "Canonical"
    vm_offer               = "0001-com-ubuntu-server-jammy"
    vm_sku                 = "22_04-lts"
    vm_version             = "latest"
    s_name                 = "myosdisk1"
    s_caching              = "ReadWrite"
    s_create_option        = "FromImage"
    s_managed_disk_type    = "Standard_LRS"
    o_computer_name        = "hostname"
    o_admin_username       = "testadmin"
    o_admin_password       = "Password1234!"

  }
  machine2 = {   #new vm is created here with all the required parameters

    vm_nicname             = "testnic2"
    vm_name                = "defender2"
    vm_location            = "centralindia"
    vm_resource_group_name = "princerg1"
    vm_size                = "Standard_D2s_v3"
    vm_publisher           = "Canonical"
    vm_offer               = "0001-com-ubuntu-server-jammy"
    vm_sku                 = "22_04-lts"
    vm_version             = "latest"
    s_name                 = "myosdisk2"
    s_caching              = "ReadWrite"
    s_create_option        = "FromImage"
    s_managed_disk_type    = "Standard_LRS"
    o_computer_name        = "hostname"
    o_admin_username       = "testadmin"
    o_admin_password       = "Password1234!"

  }
}