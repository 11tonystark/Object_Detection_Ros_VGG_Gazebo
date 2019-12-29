// Auto-generated. Do not edit!

// (in-package ros_service.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class PathRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type PathRequest
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type PathRequest
    let len;
    let data = new PathRequest(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a service object
    return 'ros_service/PathRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd41d8cd98f00b204e9800998ecf8427e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new PathRequest(null);
    return resolved;
    }
};

class PathResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.lat = null;
      this.lon = null;
    }
    else {
      if (initObj.hasOwnProperty('lat')) {
        this.lat = initObj.lat
      }
      else {
        this.lat = [];
      }
      if (initObj.hasOwnProperty('lon')) {
        this.lon = initObj.lon
      }
      else {
        this.lon = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type PathResponse
    // Serialize message field [lat]
    bufferOffset = _arraySerializer.float64(obj.lat, buffer, bufferOffset, null);
    // Serialize message field [lon]
    bufferOffset = _arraySerializer.float64(obj.lon, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type PathResponse
    let len;
    let data = new PathResponse(null);
    // Deserialize message field [lat]
    data.lat = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [lon]
    data.lon = _arrayDeserializer.float64(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 8 * object.lat.length;
    length += 8 * object.lon.length;
    return length + 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'ros_service/PathResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '43ede9fa4def9d8ab271ede42f88fcd9';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64[] lat
    float64[] lon
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new PathResponse(null);
    if (msg.lat !== undefined) {
      resolved.lat = msg.lat;
    }
    else {
      resolved.lat = []
    }

    if (msg.lon !== undefined) {
      resolved.lon = msg.lon;
    }
    else {
      resolved.lon = []
    }

    return resolved;
    }
};

module.exports = {
  Request: PathRequest,
  Response: PathResponse,
  md5sum() { return '43ede9fa4def9d8ab271ede42f88fcd9'; },
  datatype() { return 'ros_service/Path'; }
};
