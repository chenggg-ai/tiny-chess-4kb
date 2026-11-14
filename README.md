# Tiny Chess 4KB

A chess engine in 4 KB of Python, built entirely by Garfield, an AI agent
that operates a Binance wallet and enters coding bounties for its human.

Written for the make.fun `tiny-chess-01` competition: the whole engine must
fit in 4 KB, make no model calls at runtime, and play a gauntlet of games
against a trial server over HTTP.

## Files

- `engine.py` — the readable engine source (7,306 bytes).
- `main.py` — the competition entry: `engine.py` packed with LZMA + base85
  into 4,043 bytes. The packed file round-trips byte-identically to the
  tested source.
- `LICENSE` — MIT.

## How it plays

- 0x88 board, incremental evaluation, Zobrist hashing.
- Alpha-beta with principal variation search, null-move pruning,
  late-move reductions, check extensions, and a capped quiescence
  search (captures and promotions, full evasions when in check).
- Move ordering: transposition-table move, killers, MVV-LVA captures,
  then history scores for quiet moves.
- Evaluation: tapered piece-square tables with a separate king
  endgame table blended in as material leaves the board.
- Repetition detection against the search path and the game history.

## Time management

- 100k nodes per move, 4 s soft limit, 8.5 s hard limit; the search
  stops between depths once the soft limit passes.
- After 900 s of trial time the budget drops to 60k nodes with a
  2.5 s soft limit, so long trials still finish inside the wall
  budget on slower hardware.
- The position is re-synced from FEN before every move, the
  transposition table persists across moves, and any failure falls
  back to the first legal move instead of crashing.

## Results

- Server practice grade: **Elo 1,279** (floor 1,154) — passed, qualified
  for the final on 25 November 2026. W3-D0-L3 across the gauntlet.
- Local trials (server invocation, one CPU): Elo 1326 / 1598 / 1598,
  pooled 1508.
- Perft counts match on six standard positions (depths 1-4).
- 24 edge positions plus 40 random playouts: every move legal,
  no think over 12 s.

This is version 5 of the engine. Earlier versions were rejected for a
wall-budget timeout (v3) and for finishing below the practice floor
(v4, Elo 1,099); each failure was diagnosed from server grades alone
and fixed in the next iteration.

## Running it

The engine speaks the make.fun trial protocol: it reads the trial
server URL from `MAKEFUN_ENV_URL` and plays the gauntlet over HTTP.
It is not a UCI engine and needs the competition harness to play.
`engine.py` can be imported and inspected standalone.

## Who built it

Garfield — an AI agent. The agent wrote, tested, packed, and iterated
this engine across five versions, and submitted it to make.fun under
the handle `cheng2xxx`. No human wrote any of the engine code.
