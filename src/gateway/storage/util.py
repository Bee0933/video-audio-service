# pylint: disable=broad-except
# pylint: disable=unused-variable
import pika, json


def upload(f, fs, channel, access):
    try:
        fid = fs.put(f)
    except Exception as err:
        return "internal server error"

    message = {"video_fid": str(fid), "mp3_fid": None, "username": access["username"]}

    try:
        channel.basic_publish(
            exchange="",
            routing_key="video",
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
    except Exception as e:
        fs.delete(fid)
        return "internal server error"
