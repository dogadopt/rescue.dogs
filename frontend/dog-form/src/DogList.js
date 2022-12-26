import { Link } from "react-router-dom";

const DogList = ({ dogs }) => {
  return (
    <div className="dog-list">
      {dogs.map(dog => (
        <div className="dog-preview" key={dog.id} >
          <Link to={`/dogs/${dog.id}`}>
            <h2>{dog.name}</h2>
            <p>Dog is a {dog.breed}</p>
          </Link>
        </div>
      ))}
    </div>
  );
}

export default DogList; 