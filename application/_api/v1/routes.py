from flask import Blueprint, request, jsonify, render_template
from application._api.v1.models import Timezone
from application.helpers import is_number
from shapely.geometry import Point

urls_api = Blueprint('api', __name__,)

# Display all available timezones's list
@urls_api.route("/timezone", methods=['GET'])
def timezones():
    timezone = Timezone()
    # No location data available
    if 'lat' not in request.args and 'lon' not in request.args:
        result = timezone.get_all()
        return jsonify(result)
    # Missing longitude
    elif 'lat' in request.args and 'lon' not in request.args:
        return jsonify({"code": 400, "message": "Missing longitude."})
    # Missing latitude
    elif 'lat' not in request.args and 'lon' in request.args:
        return jsonify({"code": 400, "message": "Missing latitude."})
    # Both location data available
    elif 'lat' in request.args and 'lon' in request.args:
        # Check whether lat is number
        if is_number(request.args['lat']):
            lat = float(request.args['lat'])
        else:
            return jsonify({"code": 400, "message": "Latitude is not a number."})
        # Check whether lon is number
        if is_number(request.args['lon']):
            lon = float(request.args['lon'])
        else:
            return jsonify({"code": 400, "message": "Longitude is not a number."})
        # Check whether lat is between -90.0 and +90.0
        if abs(lat) < 0.0 or abs(lat) > 90.0:
            return jsonify({"code": 400, "message": "Latitude is out of the accaptable range (between -90.0 and +90.0)."})
        # Check whether lon is between -180.0 and +180.0
        if abs(lon) < 0.0 or abs(lon) > 180.0:
            return jsonify({"code": 400, "message": "Longitude is out of the accaptable range (between -180.0 and +180.0)."})

        # Check UTC timezone
        if 'utctype' in request.args:
            if request.args['utctype'] == "0":
                result = timezone.get_timezone_utc_raw(lon, lat)
            elif request.args['utctype'] == "1":
                result = timezone.get_timezone_utc(lon, lat)
            else:
                return jsonify({"code": 400, "message": "Invalid UTC type. This value can be 0 or 1."})
        else:
            result = timezone.get_timezone_world(lon, lat)

        if len(result) > 0:
            return jsonify(result)
        else:
            return jsonify({"timezone": "Unknown"})