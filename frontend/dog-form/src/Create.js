import { useState } from "react";
import { useNavigate } from 'react-router-dom'

const Create = () => {
    //state
    const [id, setId] = useState('');
    const [name, setName] = useState('');
    const [breed, setBreed] = useState(['Labrador']);
    const [isPending, setIsPending] = useState(false);
    const navigate = useNavigate();

    const handleSubmit = (e) => {
        e.preventDefault(); //stops page refresh
        const dog = {id, name, breed};
        setIsPending(true);
        
        fetch('http://localhost:8000/dogs', {
            method: 'POST',
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(dog)
        }).then(() => {
            console.log(JSON.stringify(dog));
            setIsPending(false);
            navigate('/');
        })

    }

    return ( 
        <div className="create">
            <h2>Add a New Dog</h2>
            <form onSubmit={handleSubmit}>
            <label>Dog Id</label>
                <input
                type="text"
                required
                value={id}
                onChange={(e) => setId(e.target.value)}
                />
                <label>Dog Name</label>
                <input
                type="text"
                required
                value={name}
                onChange={(e) => setName(e.target.value)}
                />
                <select
                required
                value={breed}   
                onChange={(e) => setBreed(e.target.value)}
                >
                    <option value="Labrador">Labrador</option>
                    <option value="Mastiff">Mastiff</option>
                </select> 
                { !isPending && <button>Add Dog</button> }
                { isPending && <button disabled>Adding Dog...</button> }
            </form>
        </div>
     );
}
 
export default Create;