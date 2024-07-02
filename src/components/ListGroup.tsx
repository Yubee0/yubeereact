function ListGroup() {
  const items = ["New York", "Tokyo", "Paris", "Ktm"];

  return (
    <div>
      <h1>LIST</h1>
      <ul className="list-group"></ul>

      {items.map((item) => (
        <li key={item}>{item}</li>
      ))}
    </div>
  );
}

export default ListGroup;
