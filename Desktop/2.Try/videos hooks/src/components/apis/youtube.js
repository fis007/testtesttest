import axios from "axios";

const KEY = "AIzaSyALwn5jn_WduyD8K_mjiMqkTV0gjR5zX_A";

export default axios.create({
  baseURL: "https://www.googleapis.com/youtube/v3/",
  params: {
    part: "snippet",
    type: "video",
    maxResults: 5,
    key: KEY,
  },
});
