from pathlib import Path
from .exceptions import RepositoryAlreadyExistsError


class Repository:
    def __init__(self, root: Path):
        self.root = root
        self.git_dir = root / '.mygit/'
        self.objects_dir = self.git_dir / 'objects/'
        self.refs_dir = self.git_dir / 'refs/'


    def is_initialised(self) -> bool:
        return self.git_dir.exists()
        
    
    def init(self) -> None:
        if self.is_initialised():
            raise RepositoryAlreadyExistsError(
                f"{self.root} already contains a repository.")
        
        self.git_dir.mkdir()
        self.objects_dir.mkdir()
        self.refs_dir.mkdir()

        head_path = self.git_dir / 'HEAD'
        head_path.write_text("ref: refs/heads/master")
