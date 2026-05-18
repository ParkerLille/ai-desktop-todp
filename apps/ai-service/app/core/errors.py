from fastapi import HTTPException


def raise_domain_error(code: str, message: str) -> None:
    raise HTTPException(status_code=400, detail={"code": code, "message": message})
