"""
<COSEC_API> <Events> <roll-over-count>0</roll-over-count> <seq-No>1</seq-No> <date>16/4/2014</date> <time>14:56:20</time> <event-id>457</event-id> <detail-1>0</detail-1> <detail-2>0</detail-2> <detail-3>6</detail-3> <detail-4>0</detail-4> <detail-5>0</detail-5> </Events> <Events> <roll-over-count>0</roll-over-count> <seq-No>2</seq-No> <date>16/4/2014</date> <time>14:56:20</time> <event-id>453</event-id> <detail-1>0</detail-1> <detail-2>0</detail-2> <detail-3>0</detail-3> <detail-4>0</detail-4> <detail-5>0</detail-5> </Events> <Events> <roll-over-count>0</roll-over-count> <seq-No>3</seq-No> <date>16/4/2014</date> <time>14:57:28</time> <event-id>453</event-id> <detail-1>0</detail-1> <detail-2>0</detail-2> <detail-3>0</detail-3> <detail-4>0</detail-4> <detail-5>0</detail-5> </Events> </COSEC_API>
"""

from dataclasses import dataclass
import xml.etree.ElementTree as ET
from datetime import datetime


@dataclass
class Event:
    rollOverCount: int
    seqNo: int
    date: str
    time: str
    eventId: int
    detail1: int
    detail2: int
    detail3: int
    detail4: int
    detail5: int

    @property
    def datetime(self) -> datetime:
        datetimeStr = f"{self.date} {self.time}"  # 1/3/2024 14:9:56
        return datetime.strptime(datetimeStr, "%d/%m/%Y %H:%M:%S")


def parseEvents(events: str) -> list[Event]:
    root = ET.fromstring(events)
    event_list = []
    for event_elem in root.findall("Events"):
        roll_over_count = int(event_elem.find("roll-over-count").text)
        seq_no = int(event_elem.find("seq-No").text)
        date = event_elem.find("date").text
        time = event_elem.find("time").text
        event_id = int(event_elem.find("event-id").text)
        detail1 = int(event_elem.find("detail-1").text)
        detail2 = int(event_elem.find("detail-2").text)
        detail3 = int(event_elem.find("detail-3").text)
        detail4 = int(event_elem.find("detail-4").text)
        detail5 = int(event_elem.find("detail-5").text)
        event = Event(
            roll_over_count,
            seq_no,
            date,
            time,
            event_id,
            detail1,
            detail2,
            detail3,
            detail4,
            detail5,
        )
        event_list.append(event)
    return event_list
