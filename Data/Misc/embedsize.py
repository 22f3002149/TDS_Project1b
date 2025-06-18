# write python script that extracts only embeddings from the 'embeddings.npz' file and saves them to a new file called 'extracted_embeddings.npy'.
import numpy as np
def extract_embeddings(input_file='Vercel/embeddings.npz', output_file='Misc/extracted_embeddings.npy'):
    # Load the compressed numpy file
    data = np.load(input_file, allow_pickle=True)
    
    # Extract embeddings
    embeddings = data['embeddings']
    
    # Save the embeddings to a new file
    np.save(output_file, embeddings)
    # print the shape of the embeddings
    print(f"Embeddings shape: {embeddings.shape}")
    # print the type of the embeddings
    print(f"Embeddings type: {type(embeddings)}")
    print(f"Embeddings extracted and saved to {output_file}")   

extract_embeddings()