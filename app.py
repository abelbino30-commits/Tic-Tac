import streamlit as st

st.title("❌ Tic-Tac-Toe ⭕")

# Initialize game state
if 'board' not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.turn = "X"
    st.session_state.winner = None

def check_winner(board):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None

# Display Board
cols = st.columns(3)
for i in range(9):
    with cols[i % 3]:
        if st.button(st.session_state.board[i] if st.session_state.board[i] != "" else " ", key=i):
            if st.session_state.board[i] == "" and not st.session_state.winner:
                st.session_state.board[i] = st.session_state.turn
                winner = check_winner(st.session_state.board)
                if winner:
                    st.session_state.winner = winner
                else:
                    st.session_state.turn = "O" if st.session_state.turn == "X" else "X"
                st.rerun()

# Status and Reset
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.subheader("It's a Draw!")
    else:
        st.subheader(f"Player {st.session_state.winner} Wins! 🎉")
else:
    st.write(f"Current Turn: **{st.session_state.turn}**")

if st.button("Restart Game"):
    st.session_state.board = [""] * 9
    st.session_state.turn = "X"
    st.session_state.winner = None
    st.rerun()
