import { useNavigate, useParams } from "react-router-dom";
import useFetch from "./useFetch";

const DogDetails = () => {
    const { id } = useParams();
    const { data: dog, error, isPending } = useFetch('http://localhost:8000/dogs/' + id);
    const navigate = useNavigate();

    const handleClick = () => {
        fetch('http://localhost:8000/dogs/' + dog.id, {
            method: 'DELETE'
        }).then(() => {
            navigate('/');
        })
    }

    return (
        <div className="dog-details">
            {isPending && <div>Retrieving...</div>}
            {error && <div>{error}</div>}
            {dog && (
                <article>
                    <h2>{dog.name}</h2>
                    <p>Dog breed is {dog.breed}</p>
                    <button onClick={handleClick}>Remove Dog</button>
                </article>
            )}
        </div>
    );
}

export default DogDetails;