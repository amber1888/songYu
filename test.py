import jmcomic

if __name__ == '__main__':
  properties: dict = jmcomic.JmOption.default().new_jm_client().get_album_detail("438696").get_properties_dict()
  print(properties)