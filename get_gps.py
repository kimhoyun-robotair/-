from pymavlink import mavutil

def connect_drone():
    # 드론에 연결하는 코드
    connection = mavutil.mavlink_connection('udp:127.0.0.1:14540')

    connection.wait_heartbeat()
    # 드론의 heartbeat 신호를 기다림
    print("Heartbeat received from the drone")

    return connection

def get_position_data(connection):
    # 위치 데이터를 수신받는 함수
    while True:
        # GLOBAL_POSITION_INT 메시지 수신
        msg = connection.recv_match(type="GLOBAL_POSITION_INT", blocking=True)

        if msg:
            lat = msg.lat / 1e7  # 위도 (deg)
            lon = msg.lon / 1e7  # 경도 (deg)
            #alt = msg.alt / 1000.0  # 고도 (m)
            relative_alt = msg.relative_alt / 1000.0  # 상대 고도 (m)
            vx = msg.vx / 100.0  # 북쪽으로의 속도 (m/s)
            vy = msg.vy / 100.0  # 동쪽으로의 속도 (m/s)
            vz = msg.vz / 100.0  # 아래로의 속도 (m/s)

            print(f"위도: {lat}, 경도: {lon}, 상대 고도: {relative_alt}m")
            print(f"속도 - 북쪽: {vx} m/s, 동쪽: {vy} m/s, 아래쪽: {vz} m/s")

if __name__ == "__main__":
    # 드론 연결 설정
    connection = connect_drone()
    # 데이터 수신
    get_position_data(connection)
