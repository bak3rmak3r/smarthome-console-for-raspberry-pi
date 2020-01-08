#open openhab2 dashboard or other dashboard in chromium on touch display
DISPLAY=:0 chromium-browser --fast --kiosk --noerrordialogs --disable-session-crashed-bubble 'http://IP:8080/habpanel/index.html#/view/MainDash' &
