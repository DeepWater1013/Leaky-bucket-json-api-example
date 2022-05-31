
import requests
values = """
  {
    "SKUInfo": {
      "CatalogID": 5549196,
      "SKU": "dolore occaecat",
      "Name": "ad officia reprehenderit",
      "Cost": -18128193.441653237,
      "Price": -12795496.485453308,
      "Currency": "aute cillum incididunt reprehenderit",
      "RetailPrice": -85064725.10132354,
      "SalePrice": 4346297.001677439,
      "OnSale": true,
      "Stock": -9294195.30395341
    },
    "MFGID": "labore in laborum anim aliqua",
    "ShortDescription": "in mollit",
    "ManufacturerID": -93434278,
    "ManufacturerName": "magna sit id non",
    "DistributorList": [
      {
        "DistributorID": 73796011,
        "DistributorName": "culpa Lorem tempor",
        "DistributorItemCost": -30000679.212933123,
        "DistributorItemID": "",
        "DistributorStockID": "sit sunt"
      },
      {
        "DistributorID": 65749597,
        "DistributorName": "ut in sit in est",
        "DistributorItemCost": 59802814.13794315,
        "DistributorItemID": "ut",
        "DistributorStockID": "anim elit"
      },
      {
        "DistributorID": 67615115,
        "DistributorName": "in deserunt nos",
        "DistributorItemCost": -5776140.381086051,
        "DistributorItemID": "id incididunt velit",
        "DistributorStockID": "esse Duis laboris id mag"
      },
      {
        "DistributorID": 73091730,
        "DistributorName": "ut laborum sint",
        "DistributorItemCost": 63208139.29649508,
        "DistributorItemID": "sit nostru",
        "DistributorStockID": ""
      }
    ],
    "LastUpdate": "1964-12-13T13:30:50.688Z",
    "UserID": "e",
    "GTIN": "anim pariatur",
    "CategoryList": [
      {
        "CategoryID": 25813126,
        "CategoryName": "voluptate est sint"
      }
    ],
    "ExternalIdsList": [
      {
        "ID": 29177988,
        "AdvancedOptionSufix": "nostrud",
        "ExternalId1": "anim",
        "ExternalId2": "in ea",
        "ExternalIdType": "in aliqua"
      },
      {
        "ID": 29386574,
        "AdvancedOptionSufix": "dolor inc",
        "ExternalId1": "adipisici",
        "ExternalId2": "quis in occaecat",
        "ExternalIdType": "repr"
      },
      {
        "ID": 73611044,
        "AdvancedOptionSufix": "laboris",
        "ExternalId1": "irure non amet",
        "ExternalId2": "nostrud in",
        "ExternalIdType": "a"
      },
      {
        "ID": 18470631,
        "AdvancedOptionSufix": "ex dolore cupidatat",
        "ExternalId1": "voluptate dolore",
        "ExternalId2": "eiusmod",
        "ExternalIdType": "qui cup"
      },
      {
        "ID": -58285467,
        "AdvancedOptionSufix": "occae",
        "ExternalId1": "et nostrud qui enim",
        "ExternalId2": "ve",
        "ExternalIdType": "conseq"
      }
    ],
    "CategoryExternalIdsList": [
      {
        "ID": -88729174,
        "CategoryID": 19969439,
        "ExternalId1": "pariatur",
        "ExternalIdType": "consectetur eu"
      },
      {
        "ID": 6827252,
        "CategoryID": -21147158,
        "ExternalId1": "quis mollit ad voluptate nul",
        "ExternalIdType": "ullamco aute"
      }
    ],
    "NonTaxable": false,
    "NotForSale": false,
    "Hide": true,
    "GiftCertificate": true,
    "HomeSpecial": true,
    "CategorySpecial": false,
    "NonSearchable": true,
    "GiftWrapItem": true,
    "ShipCost": 46055464.42598286,
    "Weight": 56622458.94856936,
    "Height": 39066038.03513399,
    "Width": -89917587.21531373,
    "Depth": 24223234.719419777,
    "SelfShip": true,
    "FreeShipping": false,
    "RewardPoints": -31229290,
    "RedeemPoints": 50604682,
    "DisableRewards": false,
    "StockAlert": 70440709,
    "ReorderQuantity": -4915645,
    "InStockMessage": "irure qui dolor",
    "OutOfStockMessage": "deserunt labore",
    "BackOrderMessage": "repr",
    "InventoryControl": 42231344,
    "WarehouseLocation": "labore",
    "WarehouseBin": "elit ut",
    "WarehouseAisle": "ullamco",
    "WarehouseCustom": "dolore minim dolore labore",
    "Description": "ex ipsum",
    "Keywords": "nisi aliqua do dolore",
    "ExtraField1": "aliquip occaecat",
    "ExtraField2": "in Ut culpa",
    "ExtraField3": "amet fugiat ad velit minim",
    "ExtraField4": "adipisicing Excepteur i",
    "ExtraField5": "veniam eu",
    "ExtraField6": "incididunt Lorem dolore",
    "ExtraField7": "qui nisi sint",
    "ExtraField8": "non commodo nisi ut",
    "ExtraField9": "Ut",
    "ExtraField10": "culpa sit proident",
    "ExtraField11": "nulla do ad",
    "ExtraField12": "aute",
    "ExtraField13": "dolore",
    "FeatureList": [
      {
        "FeatureID": -80732131,
        "FeatureTitle": "tempor",
        "FeatureDescription": "consectetur id"
      },
      {
        "FeatureID": -64719241,
        "FeatureTitle": "sed aute anim",
        "FeatureDescription": "aliqua labore Lorem dolore laboris"
      }
    ],
    "PluginList": {},
    "SampleEnable": false,
    "SampleName": "consequat mollit cillum",
    "SampleSKUPrefix": "elit do",
    "SamplePrice": 52647107.36979863,
    "SampleWeight": -39993658.90971256,
    "ReviewAverage": -84993379.01474324,
    "ReviewCount": -29309690,
    "MainImageFile": "fugiat esse consectetur minim dolore",
    "MainImageCaption": "in esse",
    "ThumbnailFile": "deserunt labore",
    "MediaFile": "dolore sunt",
    "AdditionalImageFile2": "qui magna voluptate eu dolore",
    "AdditionalImageCaption2": "pariatur esse Duis et occaecat",
    "AdditionalImageFile3": "cupidatat officia anim irure",
    "AdditionalImageCaption3": "dese",
    "AdditionalImageFile4": "magna anim aliqua",
    "AdditionalImageCaption4": "sed",
    "ImageGalleryList": [
      {
        "ImageGalleryID": 93947868,
        "ImageGalleryFile": "ipsum ull",
        "ImageGalleryCaption": "fugiat Lorem elit",
        "ImageGallerySorting": 46014781
      },
      {
        "ImageGalleryID": -27694772,
        "ImageGalleryFile": "Duis amet pariatur",
        "ImageGalleryCaption": "nostrud mollit ad",
        "ImageGallerySorting": 78691755
      }
    ],
    "OptionSetList": [
      {
        "OptionSetID": -69646334,
        "OptionSetName": "reprehenderit in do",
        "OptionSorting": 92270875.2891916,
        "OptionRequired": false,
        "OptionType": "ut",
        "OptionURL": "amet",
        "OptionAdditionalInformation": "labore sit nulla sint",
        "OptionSizeLimit": 36794527,
        "OptionList": [
          {
            "OptionID": 80228796,
            "OptionName": "et",
            "OptionSelected": false,
            "OptionHide": false,
            "OptionValue": 55623049.8987332,
            "OptionPartNumber": "veniam laboris dolor",
            "OptionSorting": -74392566.58937156,
            "OptionImagePath": "voluptate officia ex",
            "OptionBundleCatalogId": 10158804,
            "OptionBundleQuantity": -90825041
          },
          {
            "OptionID": -45446246,
            "OptionName": "eu Duis nisi culpa",
            "OptionSelected": true,
            "OptionHide": false,
            "OptionValue": 14593052.83329311,
            "OptionPartNumber": "dolor quis labore sed",
            "OptionSorting": 28915023.612949178,
            "OptionImagePath": "aute in",
            "OptionBundleCatalogId": -10332725,
            "OptionBundleQuantity": -64422940
          },
          {
            "OptionID": 76220317,
            "OptionName": "dolore occaecat",
            "OptionSelected": false,
            "OptionHide": true,
            "OptionValue": 81824817.61989307,
            "OptionPartNumber": "cillum pariat",
            "OptionSorting": -49748803.67471037,
            "OptionImagePath": "eu",
            "OptionBundleCatalogId": -92912523,
            "OptionBundleQuantity": -51165587
          },
          {
            "OptionID": 93721851,
            "OptionName": "qui in",
            "OptionSelected": false,
            "OptionHide": true,
            "OptionValue": -50322378.31519586,
            "OptionPartNumber": "non adipis",
            "OptionSorting": -91328384.81549959,
            "OptionImagePath": "in reprehenderit ad dol",
            "OptionBundleCatalogId": -79304784,
            "OptionBundleQuantity": -63553726
          }
        ]
      },
      {
        "OptionSetID": -35572675,
        "OptionSetName": "amet sed aliqua ullamco",
        "OptionSorting": 99700339.09028658,
        "OptionRequired": false,
        "OptionType": "Ex",
        "OptionURL": "officia eu",
        "OptionAdditionalInformation": "ullamco est voluptate Ut in",
        "OptionSizeLimit": 55369931,
        "OptionList": [
          {
            "OptionID": 13148668,
            "OptionName": "ea nostrud",
            "OptionSelected": true,
            "OptionHide": true,
            "OptionValue": -16631925.454355657,
            "OptionPartNumber": "ali",
            "OptionSorting": 54900867.54881421,
            "OptionImagePath": "dolor magna",
            "OptionBundleCatalogId": -50460761,
            "OptionBundleQuantity": 31123265
          },
          {
            "OptionID": -23701556,
            "OptionName": "Excepteur aliqua",
            "OptionSelected": false,
            "OptionHide": false,
            "OptionValue": 80544652.12607923,
            "OptionPartNumber": "officia dolor sint fugiat",
            "OptionSorting": 57703487.021828085,
            "OptionImagePath": "do mollit",
            "OptionBundleCatalogId": -25664217,
            "OptionBundleQuantity": 54667003
          }
        ]
      },
      {
        "OptionSetID": 51838031,
        "OptionSetName": "magna ad fugiat ex exerci",
        "OptionSorting": -14619305.27911593,
        "OptionRequired": false,
        "OptionType": "Duis sun",
        "OptionURL": "occaecat Duis",
        "OptionAdditionalInformation": "elit mollit",
        "OptionSizeLimit": 27273001,
        "OptionList": [
          {
            "OptionID": -29052683,
            "OptionName": "in",
            "OptionSelected": false,
            "OptionHide": true,
            "OptionValue": 23357387.488409027,
            "OptionPartNumber": "Duis ipsum reprehenderit minim",
            "OptionSorting": -21419531.206009164,
            "OptionImagePath": "proident dolor",
            "OptionBundleCatalogId": -45693313,
            "OptionBundleQuantity": 50527721
          },
          {
            "OptionID": 34411609,
            "OptionName": "anim elit ut",
            "OptionSelected": false,
            "OptionHide": false,
            "OptionValue": -72458641.55404288,
            "OptionPartNumber": "in",
            "OptionSorting": -97197595.95417297,
            "OptionImagePath": "temp",
            "OptionBundleCatalogId": -95889149,
            "OptionBundleQuantity": 70695356
          },
          {
            "OptionID": 79374564,
            "OptionName": "commodo magna laborum reprehenderit",
            "OptionSelected": true,
            "OptionHide": false,
            "OptionValue": 77296505.63058707,
            "OptionPartNumber": "adipisicing",
            "OptionSorting": -60879486.36640106,
            "OptionImagePath": "adipis",
            "OptionBundleCatalogId": 69711902,
            "OptionBundleQuantity": 79341092
          },
          {
            "OptionID": -89976635,
            "OptionName": "voluptate Excepteur velit anim labore",
            "OptionSelected": false,
            "OptionHide": true,
            "OptionValue": 84938596.4000287,
            "OptionPartNumber": "labore sed in",
            "OptionSorting": 72345152.10477185,
            "OptionImagePath": "labore irure",
            "OptionBundleCatalogId": -35456939,
            "OptionBundleQuantity": 76322969
          },
          {
            "OptionID": 83860928,
            "OptionName": "elit pariatur nostrud",
            "OptionSelected": true,
            "OptionHide": true,
            "OptionValue": -20602419.857833937,
            "OptionPartNumber": "in ipsum co",
            "OptionSorting": 38738756.258484125,
            "OptionImagePath": "anim proident",
            "OptionBundleCatalogId": -72068641,
            "OptionBundleQuantity": 88579345
          }
        ]
      },
      {
        "OptionSetID": 4271602,
        "OptionSetName": "cupidatat veniam consequat irure",
        "OptionSorting": -14739479.974589825,
        "OptionRequired": true,
        "OptionType": "dolor",
        "OptionURL": "ullamco ut",
        "OptionAdditionalInformation": "dolore exercitation adipisicing",
        "OptionSizeLimit": 17919262,
        "OptionList": [
          {
            "OptionID": -81112253,
            "OptionName": "tempor mollit non anim",
            "OptionSelected": true,
            "OptionHide": false,
            "OptionValue": 60977280.72535828,
            "OptionPartNumber": "consequat et id tempor",
            "OptionSorting": -25409869.928072527,
            "OptionImagePath": "officia ad non proident",
            "OptionBundleCatalogId": -31107751,
            "OptionBundleQuantity": -19845982
          },
          {
            "OptionID": -93858758,
            "OptionName": "est",
            "OptionSelected": false,
            "OptionHide": true,
            "OptionValue": -10270598.928671107,
            "OptionPartNumber": "Lorem proident dolor nisi",
            "OptionSorting": 68113055.15652534,
            "OptionImagePath": "in enim",
            "OptionBundleCatalogId": 24942271,
            "OptionBundleQuantity": -52934623
          }
        ]
      }
    ],
    "AdvancedOptionList": [
      {
        "AdvancedOptionCode": "id ut",
        "AdvancedOptionSufix": "minim deserunt velit ad",
        "AdvancedOptionName": "velit anim",
        "AdvancedOptionCost": 39084681.60161328,
        "AdvancedOptionStock": 34222726,
        "AdvancedOptionWeight": -88006732.64687298,
        "AdvancedOptionPrice": -88239040.15319215,
        "AdvancedOptionGTIN": "cupidatat magna et"
      }
    ],
    "RelatedProductList": [
      {
        "RelatedIndexID": 27968629,
        "RelatedProductID": -95525200,
        "RelatedProductSorting": 85427066
      },
      {
        "RelatedIndexID": 15656045,
        "RelatedProductID": 52941563,
        "RelatedProductSorting": -41967109
      },
      {
        "RelatedIndexID": -89150145,
        "RelatedProductID": -4937041,
        "RelatedProductSorting": -48278087
      },
      {
        "RelatedIndexID": 918987,
        "RelatedProductID": -51817314,
        "RelatedProductSorting": 73219839
      }
    ],
    "UpSellingItemList": [
      {
        "UpSellingIndexID": 18218798,
        "UpSellingItemID": -3621930,
        "UpSellingItemSorting": 76454676
      },
      {
        "UpSellingIndexID": -67777224,
        "UpSellingItemID": -54042324,
        "UpSellingItemSorting": 3363291
      },
      {
        "UpSellingIndexID": 77578887,
        "UpSellingItemID": -57428973,
        "UpSellingItemSorting": -95864799
      },
      {
        "UpSellingIndexID": 83383775,
        "UpSellingItemID": 57368463,
        "UpSellingItemSorting": 25004901
      }
    ],
    "DiscountList": [
      {
        "DiscountID": 74384927,
        "DiscountPriceLevel": 67653514,
        "DiscountLowbound": -12290631,
        "DiscountUpbound": 94279777,
        "DiscountPrice": 73940160.9020344,
        "DiscountPercentage": false
      },
      {
        "DiscountID": -63898723,
        "DiscountPriceLevel": -17197711,
        "DiscountLowbound": -92759546,
        "DiscountUpbound": -29938018,
        "DiscountPrice": 81190229.41320094,
        "DiscountPercentage": true
      }
    ],
    "DoNotUseCategoryOptions": false,
    "DateCreated": "1978-08-01T07:11:34.147Z",
    "ListingTemplateID": -72972336,
    "ListingTemplateName": "consequat pariatur qui",
    "LoginRequiredOptionID": -68205568,
    "LoginRequiredOptionName": "dolor anim sed amet consectetur",
    "LoginRequiredOptionRedirectTo": "ex ut commodo non",
    "AllowAccessCustomerGroupID": 89982562,
    "AllowAccessCustomerGroupName": "ea anim",
    "RMAMaxPeriod": "velit aliquip",
    "CanonicalUrl": "enim et aliqua",
    "TaxCode": "{`Zt",
    "DisplayText": "eu incididunt est sint",
    "MinimumQuantity": 69571765.83819914,
    "MaximumQuantity": 74826307.09530026,
    "AllowOnlyMultiples": false,
    "AllowFractionalQuantity": true,
    "QuantityOptions": "esse non incididunt aliquip",
    "GroupOptionsForQuantityPricing": false,
    "ApplyQuantityDiscountToOptions": true,
    "EnableMakeAnOfferFeature": false,
    "MinimumAcceptableOffer": "irure ",
    "PriceLevel1": 95063005.54670578,
    "PriceLevel1Hide": true,
    "PriceLevel2": 37967218.97883853,
    "PriceLevel2Hide": false,
    "PriceLevel3": 52483464.42231068,
    "PriceLevel3Hide": false,
    "PriceLevel4": 50607069.99263239,
    "PriceLevel4Hide": true,
    "PriceLevel5": -24448642.54785566,
    "PriceLevel5Hide": false,
    "PriceLevel6": -78375262.60727637,
    "PriceLevel6Hide": false,
    "PriceLevel7": 590307.7130752504,
    "PriceLevel7Hide": false,
    "PriceLevel8": 52722533.036241174,
    "PriceLevel8Hide": true,
    "PriceLevel9": -1128578.2064807117,
    "PriceLevel9Hide": false,
    "PriceLevel10": 72821811.21485594,
    "PriceLevel10Hide": false,
    "BuyButtonLink": "veniam non Ut",
    "ProductLink": "minim incididunt et esse",
    "Title": "consectetur dolore",
    "CustomFileName": "qui dolore veniam mollit ad",
    "RedirectLink": "fugiat dolore proident",
    "MetaTags": "aute Excepteur sed",
    "SpecialInstructions": "enim",
    "AssignKey": true,
    "ReUseKeys": true,
    "SerialList": [
      {
        "SerialID": -406765,
        "SerialUses": 81297686,
        "SerialCode": "in officia sed"
      }
    ],
    "EProductList": [
      {
        "FileNumber": 8788339,
        "FilePath": "consequat ut dolore"
      },
      {
        "FileNumber": 31017703,
        "FilePath": "mollit nostrud aliquip"
      }
    ]
  }
"""
print(values)
# headers = {
#     'Content-Type': 'application/json',
#     'Accept': 'application/json',
#     'SecureURL': '',
#     'PrivateKey': '',
#     'Token': ''
# }
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'SecureURL': 'xxxxx',
  'PrivateKey': 'xxxxxx',
  'Token': 'xxxxxx'
}
# request = Request('https://apirest.3dcart.com/3dCartWebAPI/v2/Products', data=values, headers=headers)
response_body = requests.get('https://apirest.3dcart.com/3dCartWebAPI/v2/Products')

print(response_body)
