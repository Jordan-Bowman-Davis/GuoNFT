import { NFTStorage, File } from "nft.storage"
import fs from 'fs'
import dotenv from 'dotenv'
dotenv.config()

const API_KEY = process.env.NFT_STORAGE_API_KEY

// stores metadata on IPFS using NFTStorage API
async function storeAsset() {
   const client = new NFTStorage({ token: API_KEY })
   const metadata = await client.store({
       name: 'GuoNFT',
       description: 'Stealthy!',
       image: new File(
           [await fs.promises.readFile('/Users/jordanbowman-davis/Documents/result.png')],
           'result.png',
           { type: 'image/png' }
       ),
   })
   console.log(metadata.url)
}

storeAsset()
   .then(() => process.exit(0))
   .catch((error) => {
       console.error(error);
       process.exit(1);
   });