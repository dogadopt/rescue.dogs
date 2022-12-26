import Navbar from './Navbar'
import Home from './Home'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import Create from './Create';
import DogDetails from './DogDetails';
import NotFound from './NotFound';

function App() {

  return (
    <Router>
      <div className="App">
         <Navbar />
        <div className="content">
          <Routes>
             <Route path='/' element={<Home />} />
              <Route path='/create' element={<Create />} />
              <Route path='/dogs/:id' element={<DogDetails />} />
            <Route path='*' element={<NotFound />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;