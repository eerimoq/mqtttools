import unittest

import mqttools


class FormatPacketTest(unittest.TestCase):

    maxDiff = None

    def test_format_packet(self):
        datas = [
            (
                b'\x10\x10\x00\x04MQTT\x05\x02\x00\x01\x00\x00\x03goo',
                [
                    'Received CONNECT(1) packet of 18 byte(s) with data '
                    '101000044D51545405020001000003676F6F',
                    '  ClientId:    goo',
                    '  CleanStart:  True',
                    '  WillTopic:   None',
                    '  WillMessage: None',
                    '  WillRetain:  None',
                    '  KeepAlive:   1',
                    '  UserName:    None',
                    '  Password:    None'
                ],
                'Received CONNECT(1): ClientId=goo, KeepAlive=1'
            ),
            (
                b'\x20\x03\x00\x00\x00',
                [
                    'Received CONNACK(2) packet of 5 byte(s) with data 2003000000',
                    '  SessionPresent: False',
                    '  Reason: SUCCESS(0)'
                ],
                'Received CONNACK(2): Reason=SUCCESS(0)'
            ),
            (
                b'\xc0\x00',
                [
                    'Received PINGREQ(12) packet of 2 byte(s) with data C000'
                ],
                'Received PINGREQ(12)'
            ),
            (
                b'\xd0\x00',
                [
                    'Received PINGRESP(13) packet of 2 byte(s) with data D000'
                ],
                'Received PINGRESP(13)'
            ),
            (
                b'\xe0\x0f\x80\x0d\x1f\x00\x0aSome error',
                [
                    'Received DISCONNECT(14) packet of 17 byte(s) with data '
                    'E00F800D1F000A536F6D65206572726F72',
                    '  Reason:     UNSPECIFIED_ERROR(128)',
                    '  Properties:',
                    '  Properties:',
                    '    REASON_STRING(31): Some error'
                ],
                'Received DISCONNECT(14): Reason=UNSPECIFIED_ERROR(128)'
            ),
            (
                b'\x30\x31\x00\x04\x2F\x61\x2F\x62\x00\x31\x32\x33\x34\x35'
                b'\x36\x37\x38\x39\x30\x30\x31\x32\x33\x34\x35\x36\x37\x38'
                b'\x39\x30\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x30\x30'
                b'\x31\x32\x33\x34\x35\x36\x37\x38\x39',
                [
                    'Received PUBLISH(3) packet of 51 byte(s) with data '
                    '303100042F612F6200313233343536373839303031323334353637383'
                    '930303132333435363738393030313233343536373839',
                    '  DupFlag:    False',
                    '  QoSLevel:   0',
                    '  Retain:     False',
                    '  Topic:      /a/b',
                    '  Message:    313233343536373839303031323334353637383930'
                    '303132333435363738393030313233343536373839',
                    '  Properties:'
                ],
                'Received PUBLISH(3): Topic=/a/b, Message=31323334353637383930'
                '3031323334353637383930303132333435363738393030313233343536373'
                '839'
            ),
            (
                b'\x82\x0a\x00\x01\x00\x00\x04\x2f\x61\x2f\x62\x00',
                [
                    'Received SUBSCRIBE(8) packet of 12 byte(s) with data 820A0'
                    '0010000042F612F6200',
                    '  PacketIdentifier: 1',
                    '  Subscriptions:',
                    '    Topic:             /a/b',
                    '    MaximumQoS:        0',
                    '    NoLocal:           False',
                    '    RetainAsPublished: False',
                    '    RetainHandling:    0'
                ],
                'Received SUBSCRIBE(8): Topic=/a/b'
            ),
            (
                b'\x90\x04\x00\x01\x00\x00',
                [
                    'Received SUBACK(9) packet of 6 byte(s) with data 900400010000',
                    '  PacketIdentifier: 1',
                    '  Properties:',
                    '  Reasons:',
                    '    GRANTED_QOS_0(0)'
                ],
                'Received SUBACK(9): Reason=GRANTED_QOS_0(0)'
            ),
            (
                b'\xa2\x0f\x00\x02\x00\x00\x04\x2f\x61\x2f\x62\x00\x04\x2f\x62'
                b'\x2f\x23',
                [
                    'Received UNSUBSCRIBE(10) packet of 17 byte(s) with data '
                    'A20F00020000042F612F6200042F622F23',
                    '  PacketIdentifier: 2',
                    '  Topics:',
                    '    /a/b',
                    '    /b/#'
                ],
                'Received UNSUBSCRIBE(10): Topic=/a/b, Topic=/b/#'
            ),
            (
                b'\xb0\x05\x00\x02\x00\x00\x00',
                [
                    'Received UNSUBACK(11) packet of 7 byte(s) with data '
                    'B0050002000000',
                    '  PacketIdentifier: 2',
                    '  Properties:',
                    '  Reasons:',
                    '    SUCCESS(0)',
                    '    SUCCESS(0)'
                ],
                'Received UNSUBACK(11): Reason=SUCCESS(0), Reason=SUCCESS(0)'
            )
        ]

        for message, lines, compact_lines in datas:
            self.assertEqual(
                mqttools.common.format_packet('Received', message),
                lines)
            self.assertEqual(
                mqttools.common.format_packet_compact('Received', message),
                compact_lines)
