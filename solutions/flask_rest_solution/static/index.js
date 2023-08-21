const getItems = async () => {
    const response = await fetch('http://localhost:5000/items');
    const data = await response.json();
    return data;
}
