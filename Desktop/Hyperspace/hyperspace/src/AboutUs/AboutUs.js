import React from "react";

import left from "./Images/left.png";
import right from "./Images/right.png";

function AboutUs() {
  return (
    <div
      style={{
        backgroundColor: "black",
        height: "100vh",
        fontFamily: "AvenirNextW10-Regular",
      }}
    >
      <div
        style={{
          textAlign: "left",
          display: "flex",
          alignItems: "center",
          width: "100vw",
        }}
      >
        <img style={{ height: "40vh" }} src={left} />
        <div style={{ paddingLeft: "4%", width: "40vw" }}>
          <h1 style={{ margin: "0", letterSpacing: "5px" }}>ABOUT US</h1>
          <p
            style={{
              borderTop: "1px solid white",
              borderWidth: "60%",
              margin: "0",
              paddingTop: "3%",
              fontSize: "180%",
              letterSpacing: "1px",
            }}
          >
            A community run organisation that aims to digitalize the world
          </p>
        </div>
      </div>

      <div
        style={{
          textAlign: "right",
          display: "flex",
          alignItems: "center",
          width: "100vw",
          flexDirection: "row-reverse",
        }}
      >
        <img style={{ height: "40vh" }} src={right} />

        <div style={{ paddingRight: "4%", width: "40vw" }}>
          <h1 style={{ margin: "0", letterSpacing: "5px" }}>RELATABLE</h1>
          <p
            style={{
              borderTop: "1px solid white",
              margin: "0",
              paddingTop: "3%",
              fontSize: "180%",
              letterSpacing: "1px",
            }}
          >
            As a community run organisation, we offer you an international
            experience.
          </p>
        </div>
      </div>
      <div style={{ textAlign: "left", marginLeft: "14%", fontSize: "180%" }}>
        <p>company about us</p>
      </div>
    </div>
  );
}

export default AboutUs;
