import jmcomic
import logging
import traceback

from model.manhua import ManHuaModel

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
