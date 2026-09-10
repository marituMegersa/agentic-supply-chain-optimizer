from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.supply_chain_optimizer.schemas import AgenticSupplyChainOptimizerSessionCreate, AgenticSupplyChainOptimizerSessionResponse
from app.domain.supply_chain_optimizer.service import AgenticSupplyChainOptimizerService

router = APIRouter(prefix="/api/v1/supply_chain_optimizer", tags=["Agentic Supply Chain Optimizer Domain"])

@router.post("/sessions", response_model=AgenticSupplyChainOptimizerSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticSupplyChainOptimizerSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Supply Chain Optimizer.
    """
    return AgenticSupplyChainOptimizerService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticSupplyChainOptimizerSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticSupplyChainOptimizerService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
