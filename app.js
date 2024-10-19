let vehiclesData = {};

// Fetch vehicle data from JSON
fetch('vehicles.json')
  .then(response => response.json())
  .then(data => {
    vehiclesData = data.brands;
    if (document.getElementById('indian-cars')) {
      loadIndianCars();
    }
    if (document.getElementById('usa-cars')) {
      loadUSACars();
    }
  });

// Load Indian cars into the Indian cars page
function loadIndianCars() {
  const indianCarsDiv = document.getElementById('indian-cars');
  const indianBrands = vehiclesData.filter(brand => brand.region === 'India');

  indianBrands.forEach(brand => {
    const brandHeader = document.createElement('h2');
    brandHeader.innerText = brand.name;
    indianCarsDiv.appendChild(brandHeader);
    
    brand.models.forEach(model => {
      const modelInfo = document.createElement('p');
      modelInfo.innerText = `${model.modelName} (${model.year}) - $${model.price}`;
      indianCarsDiv.appendChild(modelInfo);
    });
  });

  if (indianBrands.length === 0) {
    indianCarsDiv.innerHTML = '<p>No Indian cars available.</p>';
  }
}

// Load USA cars into the USA cars page
function loadUSACars() {
  const usaCarsDiv = document.getElementById('usa-cars');
  const usaBrands = vehiclesData.filter(brand => brand.region === 'USA');

  usaBrands.forEach(brand => {
    const brandHeader = document.createElement('h2');
    brandHeader.innerText = brand.name;
    usaCarsDiv.appendChild(brandHeader);
    
    brand.models.forEach(model => {
      const modelInfo = document.createElement('p');
      modelInfo.innerText = `${model.modelName} (${model.year}) - $${model.price}`;
      usaCarsDiv.appendChild(modelInfo);
    });
  });

  if (usaBrands.length === 0) {
    usaCarsDiv.innerHTML = '<p>No USA cars available.</p>';
  }
}

// Load models into the dropdowns for comparison
function loadModels(region) {
  const modelSelect = region === 'India' ? document.getElementById('india-model') : document.getElementById('usa-model');
  const regionBrands = vehiclesData.filter(brand => brand.region === region);

  regionBrands.forEach(brand => {
    brand.models.forEach(model => {
      const option = document.createElement('option');
      option.value = model.modelName;
      option.textContent = `${model.modelName} (${model.year}) - $${model.price}`;
      modelSelect.appendChild(option);
    });
  });
}

// Get model data for comparison
function getModelData(region, modelName) {
  const brandData = vehiclesData.find(brand => brand.region === region);
  return brandData.models.find(model => model.modelName === modelName);
}
