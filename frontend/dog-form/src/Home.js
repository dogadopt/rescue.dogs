import DogList from "./DogList";
import useFetch from "./useFetch";

const Home = () => {

    const {data: dogs, isPending, error} = useFetch('http://localhost:8000/dogs')

    return (
        <div className="home">
            <h1 className="pong">Doggos</h1>
            {error && <div>{error}</div>}
            {isPending && <div>Retrieving...</div>}
            {dogs && <DogList dogs={dogs} />}
        </div>
    );
}

export default Home;