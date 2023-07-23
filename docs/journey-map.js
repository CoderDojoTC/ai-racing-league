document.addEventListener("DOMContentLoaded", function () {
  console.log("Document is loaded and parsed");
  
  const map = document.getElementById("map");
  const tooltip = document.getElementById("tooltip");
  const regions = document.querySelectorAll(".regions .region");

  console.log(`Found ${regions.length} region elements`);

  regions.forEach((region, index) => {
    console.log(`Region ${index + 1}: `, region);

    region.addEventListener("mouseover", function (event) {
      const { x, y, width, height, text, url } = region.dataset;
      
      console.log(`Mouseover event for Region ${index + 1} at coordinates (x: ${x}, y: ${y}). Width: ${width}, Height: ${height}. Text: ${text}, URL: ${url}`);

      tooltip.innerText = text;
      tooltip.style.top = `${parseInt(y) + map.offsetTop}px`;
      tooltip.style.left = `${parseInt(x) + map.offsetLeft + parseInt(width)}px`;
      tooltip.style.display = "block";
    });

    region.addEventListener("mouseout", function (event) {
      console.log(`Mouseout event for Region ${index + 1}`);
      tooltip.style.display = "none";
    });

    region.addEventListener("click", function (event) {
      const { url } = region.dataset;
      console.log(`Click event for Region ${index + 1}, navigating to URL: ${url}`);
      window.location.href = url;
    });

    region.addEventListener("mouseover", function (event) {
      const { x, y, width, height, text, url } = region.dataset;
      console.log(`x and y values before parsing: x=${x}, y=${y}`);
      const parsedX = parseInt(x);
      const parsedY = parseInt(y);
      console.log(`x and y values after parsing: x=${parsedX}, y=${parsedY}`);
    
      // Rest of your code...
    });
    
  });
});
