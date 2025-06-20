import jmcomic
import logging
import traceback
from jmcomic import *

from model.manhua import ManHuaModel, SearchTag

logger = logging.getLogger("root")

class ManHuaService:

    @staticmethod
    def add(man_hua: ManHuaModel):
        logger.info(f"start add, album_id is: {man_hua.album_id}")
        option = jmcomic.create_option_by_file("./option.yml")
        try:
            jmcomic.download_album(f"{man_hua.album_id}", option=option)
        except Exception as e:
            logger.error("download error: {}".format(str(e)))
            logger.error("traceback: {}".format(traceback.format_exc()))
            return {"message": "fail"}
        return {"message": "ok"}

    @staticmethod
    def search(man_hua: SearchTag):
        client = JmOption.default().new_jm_client()

        # 分页查询，search_site就是禁漫网页上的【站内搜索】
        page: JmSearchPage = client.search_site(search_query=man_hua.tag, page=1)
        # page默认的迭代方式是page.iter_id_title()，每次迭代返回 albun_id, title
        result = []
        for album_id, title in page:
            print(f'[{album_id}]: {title}')
            result.append({"album_id": album_id, "title": title})

        # 直接搜索禁漫车号
        # page = client.search_site(search_query='427413')
        # album: JmAlbumDetail = page.single_album
        # print(album.tags)
        return {"message": "ok", "result": result}
