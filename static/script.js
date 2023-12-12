const BASE_URL = "http://localhost:5000/api";


function createCupcakeItem(cupcake) {
  return `
    <div>
      <li>
        <img class="cupcake-img" src="${cupcake.image}" alt="...">
        ${cupcake.flavor}, ${cupcake.size}, ${cupcake.rating}
      </li>
    </div>
  `;
}


async function showCupcakes() {
  const initialResponse = await axios.get(`${BASE_URL}/cupcakes`);
  const cupcakes = initialResponse.data.cupcakes;
  for (i in cupcakes) {
    let cupcake = createCupcakeItem(cupcakes[i])
    $("#cupcakes-list").append(cupcake);
  }
}


$("#add-cupcake").on("submit", async function (evt) {
  evt.preventDefault();
  let flavor = $("#flavor").val();
  let rating = $("#rating").val();
  let size = $("#size").val();
  let image = $("#image").val();
  let payload = {flavor, rating, size, image};
  const addCupcakeResponse = await axios.post(`${BASE_URL}/cupcakes`, payload);
  let newCupcake = $(createCupcakeItem(addCupcakeResponse.data.cupcake));
  $("#cupcakes-list").append(newCupcake);
  $("#add-cupcake").trigger("reset");
});

$(showCupcakes);
