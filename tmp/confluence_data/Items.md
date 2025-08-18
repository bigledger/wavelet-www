# Items

**Page ID**: 3297148959
**Last Updated**: 2024-11-12T20:47:42.210Z

---

## 1.1 Item Listing﻿
Under items, Create and Edit the items, or Click the item listing to see the item information.

## 1.2 Create Items﻿
To create an item click on the plus button. It takes u to the Create tab.

The screenshot above shows the mandatory fields that the user has to fill (except description and Remarks, as it is not mandatory).

## 1.2.1 Default﻿
Defaults have fields such as item code, item name, item type, sub-item type, base UOM, Product manager, remarks, item description, and currency.

Item Code - once Item Code is created it cannot be edited.

Item Name - Item Name can be edited at any time.

Base UOM - Quantities of warehouse materials (quants) are counted using the base unit of measure (UoM). Quantities in alternative units of measure are always converted to the base unit of measure for calculation purposes. For Example cm, kg, ml.

Item Description - not compulsory.

Remarks - Write your comments.

Currency - Select the currency from the dropdown list.

Product Manager - Select the Product Manager from the dropdown list.

Item type - consists of many types as follows:

1.2.1.1 Types of Items

Under the type of item, the user can select from the following Sub-item types. Each item type will have different information

a. BASIC ITEM - this is the default type that is relevant to most items.

If the user chooses the Basic item type, it will show the following Sub Item Type:

Basic Quantity

Serial Number

:info:atlassian-info#E3FCEFThe Container Measure and Container Quantity are set to 1 by default in the system so the Base Quantity for the Serial Number will be the sum of the Container Measure and Container Quantity

Batch Number

:info:atlassian-info#E3FCEFThe Container Measure is set to 1 by default in the system and the Container Quantity can be changed by the user. So the Base Quantity for the Batch will be the sum of Container Measure and Container Quantity)

Bin Number

:info:atlassian-info#E3FCEFThe Container Measure and Container Quantity can both be changed by the user. So the Base Quantity for the Bin will be the sum of Container Measure and Container Quantity)

Pin Number

Unity

b. VOUCHER - An item that is part of a Voucher. The voucher will have a "Link Voucher" option as a subtype

c. GROUPED ITEM - An item that is part of a group of related products that share common attributes like features, use, production processes, etc. It could also sometimes be the market or customer segment in which these products are sold or the prices at which they are offered. When selecting GROUPED ITEM as an item type user can add additional child items under EDIT. The grouped type has no sub-type

d. BUNDLE - If the item is a package of two or more stand-alone products sold together for a single price. These units are most commonly called stand-alone products because they are fully functioning products by themselves and can be sold separately to the consumer. Examples can be Laptop Bundles that include a keyboard and a mouse. Take note that the stock is deducted from CHILD and not PARENT. Bundle Items have only the basic quantity type set as default under the sub item type field right now.

e. COUPON - is used to record the Stock In and Stock Out of the vouchers tied to this item. If the user sets the type as coupon the item will be reflected in the VOUCHER MANAGEMENT APPLET.

f. SERVICE - If the item is a basic item without inventory tracking.

g. WARRANTY- a written guarantee, issued to the purchaser of an article by its manufacturer, promising to repair or replace it if necessary within a specified period. When selecting warranty as Item type then the additional tab will be shown in the EDIT section where users can input a warranty period. This information can be used in the POS applet when creating Invoices.

h. Gl Code - The general ledger is an accounting document that provides a general overview of an organization&rsquo;s financial transactions. An account, or general ledger (GL) code, is a number used to record business transactions in the general ledger.

j. DOC HEADER ADJUSTMENT - is used to group discounts. This will be used in the POS applet. As an Illustration, the user will attach an Item type as &ldquo;DHA&rdquo; and name it &ldquo;Extra&rdquo; to Group Discount in the POS Applet.

k. MEMBERSHIP - is used to define a member&rsquo;s attributes, dues payment schedule, and expiration settings.

l. MADE TO ORDER (MTO)- a manufacturing process where products are assembled and configured according to customer requirements.

m. Account Code

n. Digital Goods

o. Fixed Asset Register

p. Sales Contract

q. Delivery Charger

r. NSTI

s. Grouped Discount

t. Currency

:info:atlassian-info#E3FCEFSub Item Type - There are five sub-item types which are Basic Quantity, Batch Number, Serial Number, Bin Number, and Digital Goods. When a user selects any of it, it will be reflected in the POS applet. Serial Number: The Container Measure and Container Quantity are set to 1 by default in the system so the Base Quantity for the Serial Number will be the sum of the Container Measure and Container Quantity Batch Number: The Container Measure is set to 1 by default in the system and the Container Quantity can be changed by the user. So the Base Quantity for the Batch will be the sum of the Container Measure and Container Quantity Bin Number: The Container Measure and Container Quantity can both be changed by the user. So the Base Quantity for the Bin will be the sum of Container Measure and Container Quantity)

Once the item has been created more information can be added in the EDIT ITEM section. Only basic information is required to be filled in the CREATE section and afterwards, users can continue editing items in order to add more information at any time. We exclude adding more information in the CREATE section because if there is a lot of information to be added the user might forget to click save. Adding as little information as possible in the CREATE section prevents and/or reduces data being lost.

## 1.2.2 By Category﻿
Category can be set under Category Section Category Groups

## 1.2.3 Grouped Item﻿
Category can be set under Category Section Category Groups

Once all required fields are filled up, the user can press CREATE, so the item will be saved into the database and can proceed to be edited.

:info:atlassian-info#E3FCEFItems can be created manually or synced from EMP (if the user is currently using Wavelet EMP)

## 1.3 ITEMS EDIT﻿
Once the user creates an Item, it will appear in the listing. When the user wants to update the item or add more information they can click on the Item itself, a 2nd container will pop up once clicked containing the following tabs:

Main Tab

E-invoice Tab

Label Tab

Item Category Tab

Inv-item-linking Tab

Add on

Add on of

Tax Tab

Dimension Details Tab

Multi UOM Tab

Branch Linking Tab

Company Linking Tab

Pricing Scheme Tab

Manage Image Tab

Entity Pricing Tab

T2T Item Mapping Tab

Marketplace Tab

Stock Availability Tab

Stock Card Tab

Attribute Set Tab

Pages Tab

Reviews Tab

The information provided can be used in transactional Applets. Please take note that additional tabs may appear if the user chooses Grouped or Bundle as Item type.

## 1.3.1 MAIN TAB﻿
This Tab consists of general Item information such as:

Item Name - can be updated at any time

Item Code - cannot be updated

Item Type - cannot be updated

Sub Item Type - used when items are in a batch or have a serial number

GL Code - The general ledger is an accounting document that provides a general overview of an organization&rsquo;s financial transactions. An account, or general ledger (GL) code, is a number used to record business transactions in the general ledger

Base UOM - an amount in which the stock of a material is managed for example ml, kg, min

Abbreviation (Prefix) - is used in the voucher applet, in order to make it easier to view a specific group of items

EAN Code - The International Article Number is a standard describing a barcode symbology and numbering system used in global trade to identify a specific retail product type, in a specific packaging configuration, from a specific manufacturer.

Currency - a system of money in general use in a particular country. For example, USD, MYR

Status - to specify whether an item is active, inactive, or obsolete

Remarks - Write your comments

Summary - shows who created the item or who updated the item, also shows the date modified and created

## 1.3.2 E-invoice Tab﻿
This tab is for MSIC, Tax type, and UOM. Here users can do e-invoice classification.

:info:atlassian-info#E3FCEFThis can also be done under Classification in the applet menu.

## 1.3.3 Label Tab﻿
Label the items.

## 1.3.4 ITEM CATEGORY﻿
The item category tab is used to link a category to the item. Currently, have 0 - 20 categories but can add more for users upon request. Categories can be created in the &ldquo;Category&rdquo; module.

In order to add the category click &ldquo;+&rdquo;. Once clicked the 3rd container with category listings will be shown. Users can select any category that applies to the Item.

## 1.3.5 TAX TAB﻿
If tax is applicable the user can tick the checkbox. Once ticked the tax information will appear where the user can set the tax for:

Tax Country

Output Tax

Input Tax

Withholding tax

## 1.3.6 DIMENSION DETAILS TAB﻿
To fill in Product dimensions. Here user set the Height, Length, Width, Weight of the item.

## 1.3.7 MULTI UOM TAB﻿
This module allows stock items with multiple units of measurement, UOM auto conversion, and multiple UOM reports that can be later used in transactional applets. If your industry uses multi uom, you can specify here. sample of Multi UOM:

1 Box = 12 Packs

1 Packs = 10 Strips

1 Strips = 10 Tablets

The above UOM specifics the conversion of one type of UOM to another UOM, with a specific ratio.

To add Multi UOM click &ldquo;+&rdquo;. Once clicked it will open a 3rd container for the user to add UOM details

UOM - Unit of Measure. UOMs are used to quantify the inventory items and enable items to be tracked easily.

Ratio - used to specify how many items. For example:

◦ if base UOM is = &ldquo;Bottle&rdquo;, then ratio = 20 bottles

◦ The number 20 specifies the number of the items

Status - to specify whether the item is active or inactive

Base UOM - unable to edit. Users may edit it in the Main Details Tab

Sort-Code - The sort code helps identify the hierarchy of the UOM from the smallest to largest starting from 001. For example, pill would be 001 followed by the carton which would be 002 and finally box which would be 003.

For example a. pill = 001 b. carton = 002 c. box = 003

## 1.3.8 BRANCH LINKING﻿
Specify item by branch and company by linking it to them here. This tab is used to link specific branches. This function will be used in all transactional applets. for example, if a user links branches A and B then only these respective branches will be able to see the selected item in the POS applet. Branches can be created in the Organization applet.

To add a branch click &ldquo;+&rdquo;. Once clicked it will open a 3rd container for users to view listings of all branches where the user can select the preferred branches:

## 1.3.9 COMPANY LINKING﻿
Used to link companies. Specify item by branch and company by linking it to them here. Companies can be created in the Organization applet. When linking a company the item will be visible for all branches that are under the chosen Company.

In Order to add a company click &ldquo;+&rdquo;. Once clicked it will open a 3rd container for users to view listings of all companies. Here the user can select the preferred company.

:info:atlassian-info#E3FCEF if the user links company A and it has been linked to 5 BRANCHES but in Branch linking TAB the user only chooses 2 branches, then the item will be visible to ALL BRANCHES THAT IS LINKED UNDER THE COMPANY. If the user wants to link only specific branches then it needs to be chosen in the BRANCH LINKING TAB ONLY and COMPANY LINKING should remain empty.

## 1.3.10 PNS SETTLEMENT METHOD TAB﻿
The PNS Settlement Method module is used to link the Product to the PNS (Products and Services) Settlement Method.

There is a dropdown list, where the user selects the Settlement Type:

Payment Provider

Membership Point Currency

In order to add a Settlement Method click &ldquo;+&rdquo;. Once clicked it will open a 3rd container for users to choose settlement type. Here the user can select the preferred type.

## 1.3.11 PRICING SCHEME﻿
This tab is used to specify and set the prices of items. The Pricing Scheme template is added in the PRICING SCHEME module, in this tab users can add a unit price for existing pricing scheme templates. Once added this information can be used in transactional applets.

In Order to edit the price, click the item and it will open 3rd container for users to edit the Unit Price.

## 1.3.12 MANAGE IMAGE TAB﻿
This tab is used to add and categorize images based on their type for example main image, promotional image, or additional image. Users may update the period of the images they are going to be using as a reference, it has no functionality. Images may also be used in the Ecomsync applet, CP Commerce applet, and transactional applets such as POS and GRN. However, the date is only for user reference and is not meant to perform any actions.

Image type is based on ecommerce requirements. There are three image types such as:

Main Image - the image that is supposed to be displayed in the marketplace. Setting the Image type is only for the user&rsquo;s reference and a library. When syncing the item, the user has to manually select the image they wish to sync to the marketplace under attribute details.

Promotional Image - when there are certain promotions, some users might need to use special images related to the promotion, it will replace the main image. Setting the Image type is only for the user&rsquo;s reference and the library. When syncing the item, the user has to manually select the image they wish to sync to the marketplace under attribute details.

Additional images - images that end users can view when they view full item information.

As an illustration:

Item = Samsung Phone

- Main Image = the image of a Samsung phone

- Promotional Image = a themed image (based on the occasion) of a Samsung phone eg. Christmas sale

- Additional images = images of Samsung phone in different angles, the box, or additional items inside the box

## 1.3.13 ENTITY PRICING﻿
Entity Pricing module is used to set the price for the Product depending on the Entity. If u have a specific price for a specific item that has multiple suppliers, u can set it here. For instance: A single product&rsquo;s price is individual for different Entities.

To add an Entity Price click &ldquo;+&rdquo;. It will open 3rd container for users to create the Price. Then click "Entity Code" to choose the entity type.

Select the Entity type from the advanced search. There are three types of Entity to select:

Customer

Supplier

Employee

After selecting the Entity, click on the Item and it will automatically leads the user to the previous page filled in with the Entity Code and Entity Name. In this page user set the price for selected Entity.

## 1.3.14 T2T ITEM MAPPING TAB﻿
The tenant to Tenant Item Mapping module is used to map Companies, Product Codes, and Names to sync transactions

The T2T Item Mapping tab includes three tabs as follows:

Host Tenant - Main tab where the Mapping of the items is processed

Guest Tenant Item Mapping - A list of Tenants that are already Mapped

Guest Tenant Permission Listing - A list of Tenants to which permission is given for mapping. All the Permissions are given from the T2T Admin applet

To do the mapping, click the "+" button, which will lead the user to the new page, where the user selects the Tenant from the dropdown list and add the item.

## 1.3.15 MARKETPLACE TAB﻿
The Marketplace Tab is used to list the products on multiple marketplaces. This tab is to link your doc items to your Lazada Shopee or any e-commerce site. It is mainly used for Marketplaces such as Lazada, Shopee, and CP-Commerce. So the user can sell one product in various stores.

Marketplace tab includes three more tabs to do all the configurations:

Main

Other Resellers Website

Checking

Users select and add the Stores by clicking the "+" button in the Main Tab

Other Resellers Tab

This tab is used if there are resellers who are distributing your products and selling them in other different Marketplaces. Fill in the URL of the Marketplace they use.

The checking Tab is for the reports shown from the Ecomsync applet.

## 1.3.16 Add Item Images to Marketplace﻿

## 1.3.17 STOCK AVAILABILITY TAB﻿
This tab is to link your Marketplace stock balance. Stock availability tabs allow users to check whether the products are available in-store.

## 1.3.18 ATTRIBUTE SET TAB﻿
Attribute sets can be defined as a list of attributes where all the characteristics of a product are demonstrated.

## 1.3.19 PAGES TAB﻿
When the user clickss on the plus button, it will create a Post with a Draft status and an untitled post.

Users should click the created post to edit the status and the name of the post.

## 1.3.20 REVIEWS TAB﻿
The review tab allows the User or an Admin to configure reviews, settings, and votes for an item

:info:atlassian-info#E3FCEFAttributes, Pages, and Reviews tab is mostly used in E-Commerce Modules.

## 1.3.21 Bundle Config﻿
Applicable for the Bundle Item type

## 1.3.22 Child Item﻿
Applicable for the g\Grouped Item type.

## 1.3.23 Voucher Details﻿
This is Applicable for the voucher item type only.

## 1.3.24 Stock Card﻿
This is for Stock balance for the Basic Item type.
