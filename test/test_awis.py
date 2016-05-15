# -*- coding: utf-8 -*-
from awis import AwisApi
import os

def test_unicode():
  api = AwisApi(os.environ['AWS_ACCESS_ID'], os.environ['AWS_SECRET_ACCESS_KEY'])
  tree = api.category_listings("Top/World/Dansk/Børn_og_unge/Kultur")
  listings = tree.findall('.//awis:Listing', AwisApi.NS_PREFIXES)
  
  assert len(listings) > 0
