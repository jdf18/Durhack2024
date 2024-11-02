async function api_connect_to_server() {
    await fetch('/api/v1/connect', {
        method: 'POST',
        headers:{}}
    )
}

async function api_disconnect_from_server() {
    await fetch('/api/v1/disconnect', {
        method: 'POST',
        headers:{}}
    )
}

async function api_debug() {
    await fetch('/api/v1/debug', {
        method: 'POST',
        headers:{}}
    )
}

async function api_create_lobby() {
    try {
        const response = await fetch('/api/v1/create_lobby', {
            method: 'POST',
            headers:{}}
        );

        if (!response.ok) {
            throw new Error('Error when creating lobby');
        }

        const data = await response.json();
        const lobby_uid = data['lobby_uid'];
        return lobby_uid;
    } catch (error) {
        console.error("Error:", error.message);
    }
}

async function api_fire(ship_index, pos){
    try{
        const response = await fetch('/api/v1/game_fire',{
            method: 'POST',
            headers:{
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                ship_index: ship_index,
                position: pos
            })
        });
        if (!response.ok){
            throw new Error('Error when firing');
        }
    } catch(error){
        console.error("Error:", error.message);
    }
    const data = await response.json();
    const success = data['success'];
    return success;
}

async function api_is_my_turn(){
    try{
        const response = await fetch('/api/v1/game_is_my_turn',{
            method: 'POST',
            headers:{}
        });
        if (!response.ok){
            throw new Error('Error when getting turn');
        }
    } catch(error){
        console.error("Error:", error.message);
    }
    const data = await response.json();
    const is_my_turn = data['is_my_turn'];
    return is_my_turn;
}

async function api_move(ship_index, count){
    try{
        const response = await fetch('/api/v1/game_move',{
            method: 'POST',
            headers:{
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                ship_index: ship_index,
                count: count
            })
        });
        if (!response.ok){
            throw new Error('Error when moving');
        }
    } catch(error){
        console.error("Error:", error.message);
    }
    const data = await response.json();
    const success = data['success'];
    return success;
}

async function api_rotate(ship_index, is_anti_clockwise){
    try{
        const response = await fetch('/api/v1/game_rotate',{
            method: 'POST',
            headers:{
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                ship_index: ship_index,
                is_acw: is_anti_clockwise
            })
        });
        if (!response.ok){
            throw new Error('Error when rotating');
        }
    } catch(error){
        console.error("Error:", error.message);
    }
    const data = await response.json();
    const success = data['success'];
    return success;
}

async function has_game_finished(){
    try{
        const response = await fetch('/api/v1/game_has_game_finished',{
            method: 'POST',
            headers:{}
        });
        if (!response.ok){
            throw new Error('Error when getting game finished');
        }
    } catch(error){
        console.error("Error:", error.message);
    }
    const data = await response.json();
    const has_game_finished = data['has_game_finished'];
    return has_game_finished;
}

async function is_winner(){
    try{
        const response = await fetch('/api/v1/game_is_winner',{
            method: 'POST',
            headers:{}
        });
        if (!response.ok){
            throw new Error('Error when getting game winner');
        }
    } catch(error){
        console.error("Error:", error.message);
    }
    const data = await response.json();
    const is_winner = data['is_winner'];
    return is_winner;
}

async function get_available_ships(){
    try{
        const response = await fetch('/api/v1/game_get_available_ships',{
            method: 'POST',
            headers:{}
        });
        if (!response.ok){
            throw new Error('Error when getting available ships');
        }
    } catch(error){
        console.error("Error:", error.message);
    }
    const data = await response.json();
    return data;
}