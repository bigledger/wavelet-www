---
description: Document Item Types 3225452915 2021-07-12T09:07:01.
tags:
- user-guide
- tutorial
title: Document Item Types
weight: 10
---

# Document Item Types
**Page ID**: 3225452915
**Last Updated**: 2021-07-12T09:07:01.033Z
Basic Item refers to an FI-item, an individual item having a one-to-one mapping with an INV Item;
Kit , where  a basic item has 1 to 1 mapping with INV item, however this has child components. The kitting process/reverse kitting process will apply. 1 Kit (Kit-A) may have A1, A2, A3, A4 child items, which will be deducted from the stock balance, while a Kit-A quantity will also increase by 1 (this constitutes one of the main differences between Kit and a Grouped item).
Grouped item is applicable for those cases when an item has dimensions (e.g. size, colour etc). This refers to the grouping of the basic items. For example, T-shirt - Yellow/Blue/Red - size 3/4/5 : When the customer selects a T-shirt, he/she is presented with options (e.g. colours & sizes).  (Ratio = 1, i.e. only to choose one from the list). A grouping of basic FI-items and it has a ratio of 1, meaning from this grouping, you only select 1 basic FI-item. 
Package : Implies one-to-many relationship : This FI-item is mapped to many INV items. It has a one to many relationship with INV items. The stock quantity of the individual INV items is not deducted until the package is sold. 
Being the most complicated among all, Bundle can contain individual components as either basic items, Kit, grouped items or package. Therefore having multiple GenDocLines unlike the previous 4. The bundle currently supports 2 levels.