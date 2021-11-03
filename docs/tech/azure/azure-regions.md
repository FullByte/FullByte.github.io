# Azure Regions

Infrastructure Map: <https://infrastructuremap.microsoft.com>

## Locations Naming

Overview of regions in azure and their official short name:

| Continent     | Country              | Name                 | Location           | Short Name | Short Name (Country First) |
|---------------|----------------------|----------------------|--------------------|------------|----------------------------|
| Africa        | South Africa North   | southafricanorth     | sfno               | sfno       |                            |
| Africa        | South Africa West    | southafricawest      | sfwe               | sfwe       |                            |
| Asia          | East Asia            | eastasia             | eaas               | asea       |                            |
| Asia          | Southeast Asia       | southeastasia        | seas               | assoea     |                            |
| Asia          | Japan                | Japan West           | japanwest          | jawe       | jawe                       |
| Asia          | Japan                | Japan East           | japaneast          | jaea       | jaea                       |
| Asia          | India                | South India          | southindia         | soin       | inso                       |
| Asia          | India                | Central India        | centralindia       | cnin       | incn                       |
| Asia          | India                | West India           | westindia          | wein       | inwe                       |
| Asia          | Korea                | Korea Central        | koreacentral       | krcn       | krcn                       |
| Asia          | Korea                | Korea South          | koreasouth         | krso       | krso                       |
| Asia          | United Arab Emirates | UAE Central          | uaecentral         | aecn       | aecn                       |
| Asia          | United Arab Emirates | UAE North            | uaenorth           | aeno       | aeno                       |
| Australia     | Australia            | Australia East       | australiaeast      | auea       | auea                       |
| Australia     | Australia            | Australia Southeast  | australiasoutheast | ause       | ause                       |
| Australia     | Australia            | Australia Central    | australiacentral   | aucn       | aucn                       |
| Australia     | Australia            | Australia Central 2  | australiacentral2  | aucn2      | aucn3                      |
| Europe        | North Europe         | northeurope          | noeu               | euno       |                            |
| Europe        | West Europe          | westeurope           | weeu               | euwe       |                            |
| Europe        | United Kingdom       | UK South             | uksouth            | ukso       | ukso                       |
| Europe        | United Kingdom       | UK West              | ukwest             | ukwe       | ukwe                       |
| Europe        | France               | France Central       | francecentral      | frcn       | frcn                       |
| Europe        | France               | France South         | francesouth        | frso       | frso                       |
| Europe        | Swizterland          | Switzerland North    | switzerlandnorth   | chno       | chno                       |
| Europe        | Swizterland          | Switzerland West     | switzerlandwest    | chwe       | chwe                       |
| Europe        | Germany              | Germany North        | germanynorth       | deno       | deno                       |
| Europe        | Germany              | Germany West Central | germanywestcentral | dewecn     | dewecn                     |
| Europe        | Norway               | Norway West          | norwaywest         | nowe       | nowe                       |
| Europe        | Norway               | Norway East          | norwayeast         | noea       | noea                       |
| North America | United States        | Central US           | centralus          | cnus       | uscn                       |
| North America | United States        | East US              | eastus             | eaus       | usea                       |
| North America | United States        | East US 2            | eastus2            | eaus2      | usea2                      |
| North America | United States        | West US              | westus             | weus       | uswe                       |
| North America | United States        | North Central US     | northcentralus     | nocnus     | usnocn                     |
| North America | United States        | South Central US     | southcentralus     | socnus     | ussocn                     |
| North America | Central America      | Canada Central       | canadacentral      | cacn       | cacn                       |
| North America | Central America      | Canada East          | canadaeast         | caea       | caea                       |
| North America | United States        | West Central US      | westcentralus      | wecnus     | uswecn                     |
| North America | United States        | West US 2            | westus2            | weus2      | uswe2                      |
| South America | Brazil               | Brazil South         | brazilsouth        | brso       | brso                       |

## Geography and Regions

According to the [azure global-infrastructure](https://azure.microsoft.com/en-us/global-infrastructure) we have [geography](https://azure.microsoft.com/en-us/global-infrastructure/data-residency) in which there are [regions](https://azure.microsoft.com/en-us/global-infrastructure/services/) which is a set of datacenters:

- An Azure **geography** is a discrete market, typically containing at least one or more regions, that preserves data residency and compliance boundaries. Geographies allow customers with specific data-residency and compliance needs to keep their data and applications close. Geographies are fault-tolerant to withstand complete region failure through their connection to the dedicated high-capacity networking infrastructure of Azure.
- An Azure **region** is a set of datacenters, deployed within a latency-defined perimeter and connected through a dedicated regional low-latency network. With more global regions than any other cloud provider, Azure gives customers the flexibility to deploy applications where they need. An Azure region has discrete pricing and service availability.
- Azure **datacenters** are unique physical buildings—located all over the globe—that house a group of networked computer servers.

The following command shows us all available regions: ```az account list-locations -o table```

| DisplayName              | Name                | RegionalDisplayName                   |
|--------------------------|---------------------|---------------------------------------|
| East US                  | eastus              | (US) East US                          |
| East US 2                | eastus2             | (US) East US 2                        |
| South Central US         | southcentralus      | (US) South Central US                 |
| West US 2                | westus2             | (US) West US 2                        |
| West US 3                | westus3             | (US) West US 3                        |
| Australia East           | australiaeast       | (Asia Pacific) Australia East         |
| Southeast Asia           | southeastasia       | (Asia Pacific) Southeast Asia         |
| North Europe             | northeurope         | (Europe) North Europe                 |
| Sweden Central           | swedencentral       | (Europe) Sweden Central               |
| UK South                 | uksouth             | (Europe) UK South                     |
| West Europe              | westeurope          | (Europe) West Europe                  |
| Central US               | centralus           | (US) Central US                       |
| North Central US         | northcentralus      | (US) North Central US                 |
| West US                  | westus              | (US) West US                          |
| South Africa North       | southafricanorth    | (Africa) South Africa North           |
| Central India            | centralindia        | (Asia Pacific) Central India          |
| East Asia                | eastasia            | (Asia Pacific) East Asia              |
| Japan East               | japaneast           | (Asia Pacific) Japan East             |
| Jio India West           | jioindiawest        | (Asia Pacific) Jio India West         |
| Korea Central            | koreacentral        | (Asia Pacific) Korea Central          |
| Canada Central           | canadacentral       | (Canada) Canada Central               |
| France Central           | francecentral       | (Europe) France Central               |
| Germany West Central     | germanywestcentral  | (Europe) Germany West Central         |
| Norway East              | norwayeast          | (Europe) Norway East                  |
| Switzerland North        | switzerlandnorth    | (Europe) Switzerland North            |
| UAE North                | uaenorth            | (Middle East) UAE North               |
| Brazil South             | brazilsouth         | (South America) Brazil South          |
| Central US (Stage)       | centralusstage      | (US) Central US (Stage)               |
| East US (Stage)          | eastusstage         | (US) East US (Stage)                  |
| East US 2 (Stage)        | eastus2stage        | (US) East US 2 (Stage)                |
| North Central US (Stage) | northcentralusstage | (US) North Central US (Stage)         |
| South Central US (Stage) | southcentralusstage | (US) South Central US (Stage)         |
| West US (Stage)          | westusstage         | (US) West US (Stage)                  |
| West US 2 (Stage)        | westus2stage        | (US) West US 2 (Stage)                |
| Asia                     | asia                | Asia                                  |
| Asia Pacific             | asiapacific         | Asia Pacific                          |
| Australia                | australia           | Australia                             |
| Brazil                   | brazil              | Brazil                                |
| Canada                   | canada              | Canada                                |
| Europe                   | europe              | Europe                                |
| France                   | france              | France                                |
| Germany                  | germany             | Germany                               |
| Global                   | global              | Global                                |
| India                    | india               | India                                 |
| Japan                    | japan               | Japan                                 |
| Korea                    | korea               | Korea                                 |
| Norway                   | norway              | Norway                                |
| South Africa             | southafrica         | South Africa                          |
| Switzerland              | switzerland         | Switzerland                           |
| United Arab Emirates     | uae                 | United Arab Emirates                  |
| United Kingdom           | uk                  | United Kingdom                        |
| United States            | unitedstates        | United States                         |
| East Asia (Stage)        | eastasiastage       | (Asia Pacific) East Asia (Stage)      |
| Southeast Asia (Stage)   | southeastasiastage  | (Asia Pacific) Southeast Asia (Stage) |
| Central US EUAP          | centraluseuap       | (US) Central US EUAP                  |
| East US 2 EUAP           | eastus2euap         | (US) East US 2 EUAP                   |
| West Central US          | westcentralus       | (US) West Central US                  |
| South Africa West        | southafricawest     | (Africa) South Africa West            |
| Australia Central        | australiacentral    | (Asia Pacific) Australia Central      |
| Australia Central 2      | australiacentral2   | (Asia Pacific) Australia Central 2    |
| Australia Southeast      | australiasoutheast  | (Asia Pacific) Australia Southeast    |
| Japan West               | japanwest           | (Asia Pacific) Japan West             |
| Jio India Central        | jioindiacentral     | (Asia Pacific) Jio India Central      |
| Korea South              | koreasouth          | (Asia Pacific) Korea South            |
| South India              | southindia          | (Asia Pacific) South India            |
| West India               | westindia           | (Asia Pacific) West India             |
| Canada East              | canadaeast          | (Canada) Canada East                  |
| France South             | francesouth         | (Europe) France South                 |
| Germany North            | germanynorth        | (Europe) Germany North                |
| Norway West              | norwaywest          | (Europe) Norway West                  |
| Switzerland West         | switzerlandwest     | (Europe) Switzerland West             |
| UK West                  | ukwest              | (Europe) UK West                      |
| UAE Central              | uaecentral          | (Middle East) UAE Central             |
| Brazil Southeast         | brazilsoutheast     | (South America) Brazil Southeast      |

We can filter all regions of a given geography e.g. Europe: ```az account list-locations --query "[? contains(regionalDisplayName,'(Europe)')]" -o table```

| Name               | DisplayName          | RegionalDisplayName           |
|--------------------|----------------------|-------------------------------|
| northeurope        | North Europe         | (Europe) North Europe         |
| swedencentral      | Sweden Central       | (Europe) Sweden Central       |
| uksouth            | UK South             | (Europe) UK South             |
| westeurope         | West Europe          | (Europe) West Europe          |
| francecentral      | France Central       | (Europe) France Central       |
| germanywestcentral | Germany West Central | (Europe) Germany West Central |
| norwayeast         | Norway East          | (Europe) Norway East          |
| switzerlandnorth   | Switzerland North    | (Europe) Switzerland North    |
| francesouth        | France South         | (Europe) France South         |
| germanynorth       | Germany North        | (Europe) Germany North        |
| norwaywest         | Norway West          | (Europe) Norway West          |
| switzerlandwest    | Switzerland West     | (Europe) Switzerland West     |
| ukwest             | UK West              | (Europe) UK West              |

To get an overview of all locations we can run the following command:

```sh
az account list-locations --query "[?metadata.regionType=='Physical'] .{Geography:metadata.geographyGroup, RegionName:name, PairedRegion:metadata.pairedRegion[0].name, Location:metadata.physicalLocation, lat:metadata.latitude, long:metadata.longitude}" -o table
```

| Geography     | RegionName         | PairedRegion       | Location        | Lat        | Long        |
|---------------|--------------------|--------------------|-----------------|------------|-------------|
| US            | eastus             | westus             | Virginia        | 37.3719    | -79.8164    |
| US            | eastus2            | centralus          | Virginia        | 36.6681    | -78.3889    |
| US            | southcentralus     | northcentralus     | Texas           | 29.4167    | -98.5       |
| US            | westus2            | westcentralus      | Washington      | 47.233     | -119.852    |
| US            | westus3            | eastus             | Phoenix         | 33.448376  | -112.074036 |
| Asia Pacific  | australiaeast      | australiasoutheast | New South Wales | -33.86     | 151.2094    |
| Asia Pacific  | southeastasia      | eastasia           | Singapore       | 1.283      | 103.833     |
| Europe        | northeurope        | westeurope         | Ireland         | 53.3478    | -6.2597     |
| Europe        | swedencentral      | swedensouth        | Gävle           | 60.67488   | 17.14127    |
| Europe        | uksouth            | ukwest             | London          | 50.941     | -0.799      |
| Europe        | westeurope         | northeurope        | Netherlands     | 52.3667    | 4.9         |
| US            | centralus          | eastus2            | Iowa            | 41.5908    | -93.6208    |
| US            | northcentralus     | southcentralus     | Illinois        | 41.8819    | -87.6278    |
| US            | westus             | eastus             | California      | 37.783     | -122.417    |
| Africa        | southafricanorth   | southafricawest    | Johannesburg    | -25.731340 | 28.218370   |
| Asia Pacific  | centralindia       | southindia         | Pune            | 18.5822    | 73.9197     |
| Asia Pacific  | eastasia           | southeastasia      | Hong Kong       | 22.267     | 114.188     |
| Asia Pacific  | japaneast          | japanwest          | Tokyo, Saitama  | 35.68      | 139.77      |
| Asia Pacific  | jioindiawest       | jioindiacentral    | Jamnagar        | 22.470701  | 70.05773    |
| Asia Pacific  | koreacentral       | koreasouth         | Seoul           | 37.5665    | 126.9780    |
| Canada        | canadacentral      | canadaeast         | Toronto         | 43.653     | -79.383     |
| Europe        | francecentral      | francesouth        | Paris           | 46.3772    | 2.3730      |
| Europe        | germanywestcentral | germanynorth       | Frankfurt       | 50.110924  | 8.682127    |
| Europe        | norwayeast         | norwaywest         | Norway          | 59.913868  | 10.752245   |
| Europe        | switzerlandnorth   | switzerlandwest    | Zurich          | 47.451542  | 8.564572    |
| Middle East   | uaenorth           | uaecentral         | Dubai           | 25.266666  | 55.316666   |
| South America | brazilsouth        | southcentralus     | Sao Paulo State | -23.55     | -46.633     |
| US            | centraluseuap      | eastus2euap        |                 | 41.5908    | -93.6208    |
| US            | eastus2euap        | centraluseuap      |                 | 36.6681    | -78.3889    |
| US            | westcentralus      | westus2            | Wyoming         | 40.890     | -110.234    |
| Africa        | southafricawest    | southafricanorth   | Cape Town       | -34.075691 | 18.843266   |
| Asia Pacific  | australiacentral   | australiacentral   | Canberra        | -35.3075   | 149.1244    |
| Asia Pacific  | australiacentral2  | australiacentral2  | Canberra        | -35.3075   | 149.1244    |
| Asia Pacific  | australiasoutheast | australiaeast      | Victoria        | -37.8136   | 144.9631    |
| Asia Pacific  | japanwest          | japaneast          | Osaka           | 34.6939    | 135.5022    |
| Asia Pacific  | jioindiacentral    | jioindiawest       | Nagpur          | 21.146633  | 79.08886    |
| Asia Pacific  | koreasouth         | koreacentral       | Busan           | 35.1796    | 129.0756    |
| Asia Pacific  | southindia         | centralindia       | Chennai         | 12.9822    | 80.1636     |
| Asia Pacific  | westindia          | southindia         | Mumbai          | 19.088     | 72.868      |
| Canada        | canadaeast         | canadacentral      | Quebec          | 46.817     | -71.217     |
| Europe        | francesouth        | francecentral      | Marseille       | 43.8345    | 2.1972      |
| Europe        | germanynorth       | germanywestcentral | Berlin          | 53.073635  | 8.806422    |
| Europe        | norwaywest         | norwayeast         | Norway          | 58.969975  | 5.733107    |
| Europe        | switzerlandwest    | switzerlandnorth   | Geneva          | 46.204391  | 6.143158    |
| Europe        | ukwest             | uksouth            | Cardiff         | 53.427     | -3.084      |
| Middle East   | uaecentral         | uaenorth           | Abu Dhabi       | 24.466667  | 54.366669   |
| South America | brazilsoutheast    | brazilsouth        | Rio             | -22.90278  | -43.2075    |

The list-locations result also has “logical” instead of physical entries which seems to include staging regions and is yet another set of regions/geographies. Running this command

```sh
az account list-locations --query "[?metadata.regionType=='Logical']" -o table
```

| Name                | DisplayName              | RegionalDisplayName                   |
|---------------------|--------------------------|---------------------------------------|
| centralusstage      | Central US (Stage)       | (US) Central US (Stage)               |
| eastusstage         | East US (Stage)          | (US) East US (Stage)                  |
| eastus2stage        | East US 2 (Stage)        | (US) East US 2 (Stage)                |
| northcentralusstage | North Central US (Stage) | (US) North Central US (Stage)         |
| southcentralusstage | South Central US (Stage) | (US) South Central US (Stage)         |
| westusstage         | West US (Stage)          | (US) West US (Stage)                  |
| westus2stage        | West US 2 (Stage)        | (US) West US 2 (Stage)                |
| asia                | Asia                     | Asia                                  |
| asiapacific         | Asia Pacific             | Asia Pacific                          |
| australia           | Australia                | Australia                             |
| brazil              | Brazil                   | Brazil                                |
| canada              | Canada                   | Canada                                |
| europe              | Europe                   | Europe                                |
| france              | France                   | France                                |
| germany             | Germany                  | Germany                               |
| global              | Global                   | Global                                |
| india               | India                    | India                                 |
| japan               | Japan                    | Japan                                 |
| korea               | Korea                    | Korea                                 |
| norway              | Norway                   | Norway                                |
| southafrica         | South Africa             | South Africa                          |
| switzerland         | Switzerland              | Switzerland                           |
| uae                 | United Arab Emirates     | United Arab Emirates                  |
| uk                  | United Kingdom           | United Kingdom                        |
| unitedstates        | United States            | United States                         |
| eastasiastage       | East Asia (Stage)        | (Asia Pacific) East Asia (Stage)      |
| southeastasiastage  | Southeast Asia (Stage)   | (Asia Pacific) Southeast Asia (Stage) |

According to [azure global-infrastructure](https://azure.microsoft.com/en-us/global-infrastructure/geographies/#overview)

```txt
Africa
Asia Pacific
Australia
Austria
Azure Government
Brazil
Canada
Chile
China
Denmark
Europe
France
Germany
Greece
India
Indonesia
Israel
Italy
Japan
Korea
Malaysia
Mexico
New Zealand
Norway
Poland
Qatar
Spain
Sweden
Switzerland
Taiwan
United Arab Emirates
United Kingdom
United States
```

The command ```az account list-locations | jq 'map(.metadata.geographyGroup)' | sort | uniq``` returns the following unique list of geographies:

```txt
Africa
Asia Pacific
Canada
Europe
Middle East
null
South America
US
```

`null` shows that not all entries have a geographyGroup defined.

## Azure Public IPs

Tools

- [Azure service tags](https://azservicetags.azurewebsites.net)

Documentation

- [Allowed IP addresses and domain URLs](https://docs.microsoft.com/en-us/azure/devops/organizations/security/allow-list-ip-url)
- [Service Tags Overview](https://docs.microsoft.com/en-us/azure/virtual-network/service-tags-overview)

Download Public IP Lists:

- [Azure IP Ranges and Service Tags – Public Cloud](https://www.microsoft.com/en-us/download/details.aspx?id=56519)
- [Azure IP Ranges and Service Tags – US Government Cloud](https://www.microsoft.com/en-us/download/details.aspx?id=57063)
- [Azure IP Ranges and Service Tags – Germany Cloud](https://www.microsoft.com/en-us/download/details.aspx?id=57064)
- [Azure IP Ranges and Service Tags – China Cloud](http://www.microsoft.com/en-us/download/details.aspx?id=57062)

Public IP History

| Date     | Public                                             | US Gov                                                        | Germany                                                     | China                                                    |
|----------|----------------------------------------------------|---------------------------------------------------------------|-------------------------------------------------------------|----------------------------------------------------------|
| 20170911 | [download](public-ip/AzurePublicIPs_20170911.xml)  | N/A                                                           | N/A                                                         | N/A                                                      |
| 20180305 | [download](public-ip/AzurePublicIPs_20180305.xml)  | N/A                                                           | N/A                                                         | N/A                                                      |
| 20180111 | N/A                                                | N/A                                                           | [download](public-ip/AzurePublicIPs_Germnany_20180111.xml)  | [download](public-ip/AzurePublicIPs_China_20180111.xml)  |
| 20190617 | [download](public-ip/AzurePublicIPs_20190617.xml)  | N/A                                                           | N/A                                                         | N/A                                                      |
| 20200824 | [download](public-ip/AzurePublicIPs_20200824.xml)  | N/A                                                           | [download](public-ip/AzurePublicIPs_Germnany_20200824.xml)  | N/A                                                      |
| 20210816 | [download](public-ip/AzurePublicIPs_20210816.json) | [download](public-ip/AzurePublicIPs_Government_20210816.json) | [download](public-ip/AzurePublicIPs_Germnany_20210816.json) | [download](public-ip/AzurePublicIPs_China_20210816.json) |
| 20210920 | [download](public-ip/AzurePublicIPs_20210920.json) | N/A                                                           | N/A                                                         | N/A                                                      |
| 20211101 | [download](public-ip/AzurePublicIPs_20211101.json) | [download](public-ip/AzurePublicIPs_Government_20211101.json) | [download](public-ip/AzurePublicIPs_Germnany_20211101.json) | N/A                                                      |

Further (deprecated) Files

- [geoloc-Microsoft.csv](public-ip/geoloc-Microsoft.csv)
- [msft-public-ips.csv](public-ip/msft-public-ips.csv)
