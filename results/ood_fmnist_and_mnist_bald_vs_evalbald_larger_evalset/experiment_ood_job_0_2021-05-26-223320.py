store = {}
store['timestamp']=1622064800
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=0']
store['commit']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['github_url']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=0
store['worker_id']=0
store['num_workers']=80
store['config']={'seed': 1234, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastFashionMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 3792, 5573, 45567, 10508, 2728, 21423, 396, 49512, 31444]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.173092842102051})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.45434308052063})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.655754566192627})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.6076624393463135})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.6232244968414307})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.793619155883789})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 3.1201162338256836})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.905630111694336})
store['active_learning_steps'][0]['training']['best_epoch']=5
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.7043, 'crossentropy': 2.4752515625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.2784311771392822})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.435133457183838})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.4288599491119385})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.3982796669006348})
store['active_learning_steps'][0]['eval_training']['best_epoch']=1
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 47689], ['id', 48043], ['id', 16645], ['ood', 15832], ['ood', 30689]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.9600201352993061, 1.719460557133433, 2.1975385912961665, 2.4815589399533167, 2.6566554097805826]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.822506308555603})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.9946037530899048})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.406674861907959})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.5348615646362305})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.2889084815979004})
store['active_learning_steps'][1]['training']['best_epoch']=2
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6595, 'crossentropy': 1.97858125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.3399641513824463})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.2897400856018066})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.2991299629211426})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.3709945678710938})
store['active_learning_steps'][1]['eval_training']['best_epoch']=1
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 38788], ['id', 33749], ['id', 32782], ['id', 22588], ['id', 34846]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6151163306115901, 1.123950885887706, 1.5125668682856244, 1.7850978110399707, 1.9887523961837132]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.4968833923339844})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.8389562368392944})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.9180984497070312})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 2.1255884170532227})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7232, 'crossentropy': 1.4496025390625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1815476417541504})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.1945226192474365})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.1918134689331055})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 57236], ['id', 45666], ['id', 46832], ['id', 59377], ['ood', 6574]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5900508039919972, 1.1218823884808504, 1.5545013196451674, 1.8845651807782682, 2.1258963883378303]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.4011437892913818})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.0040555000305176})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.9342048168182373})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.020819902420044})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.163208484649658})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.389781951904297})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.080498695373535})
store['active_learning_steps'][3]['training']['best_epoch']=4
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7194, 'crossentropy': 1.953295703125}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.3515546321868896})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.382737159729004})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.373321771621704})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.4287991523742676})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.5410951375961304})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.426602840423584})
store['active_learning_steps'][3]['eval_training']['best_epoch']=4
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 4145], ['id', 5736], ['id', 8116], ['id', 12964], ['id', 5328]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7696613942574546, 1.3557362426392525, 1.8201243309199349, 2.1331158364672422, 2.3614187319095477]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.3383312225341797})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.6580528020858765})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.7250473499298096})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.6038109064102173})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.960862636566162})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.9972550868988037})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.8869984149932861})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.9952261447906494})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.9590482711791992})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.019944667816162})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 2.2309980392456055})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.9339120388031006})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 2.2056078910827637})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 2.194715976715088})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.348170280456543})
store['active_learning_steps'][4]['training']['best_epoch']=12
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7502, 'crossentropy': 1.865959375}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.1791245937347412})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.2379992008209229})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.3738906383514404})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.3425543308258057})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.2766752243041992})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.3137446641921997})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.3495745658874512})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.3783798217773438})
store['active_learning_steps'][4]['eval_training']['best_epoch']=5
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 19185], ['id', 24312], ['id', 24669], ['id', 53880], ['id', 49892]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8862991989324844, 1.5432527328886518, 2.0770309390643185, 2.4482821137761217, 2.670471292054163]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.3005728721618652})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.4943293333053589})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.6555843353271484})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.8738834857940674})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.787636637687683})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.996917486190796})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.9382336139678955})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 2.0246100425720215})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 2.1263365745544434})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.9006723165512085})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 2.3306992053985596})
store['active_learning_steps'][5]['training']['best_epoch']=8
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7437, 'crossentropy': 1.8472466796875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.36081063747406})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.2897331714630127})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.3624303340911865})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.3802762031555176})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.3060133457183838})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.378462791442871})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.3669358491897583})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.3110361099243164})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.2260562181472778})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.3194186687469482})
store['active_learning_steps'][5]['eval_training']['best_epoch']=9
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 26477], ['id', 4866], ['id', 13703], ['id', 47936], ['id', 57421]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.6858851053513002, 1.3004689854958569, 1.8083559999212557, 2.1776453497581016, 2.4329852976770185]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.2871026992797852})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.5998938083648682})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.6256399154663086})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.8414040803909302})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.8210654258728027})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.180907726287842})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.952497959136963})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.8899691104888916})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.934804081916809})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 2.052912712097168})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 2.1740126609802246})
store['active_learning_steps'][6]['training']['best_epoch']=8
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7406, 'crossentropy': 1.813509375}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.3235526084899902})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.4671536684036255})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.324047565460205})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.3209086656570435})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.4576870203018188})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.3635808229446411})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 26907], ['id', 21421], ['id', 17779], ['id', 1239], ['id', 25644]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7562722006911606, 1.3499975955926455, 1.7929433263636314, 2.0776488539047886, 2.2661370049344196]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.2905128002166748})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.4343914985656738})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.5752792358398438})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.64736008644104})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.7240374088287354})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7385, 'crossentropy': 1.4060853515625}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.0789358615875244})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 0.9982129335403442})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 0.9394850730895996})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 0.9155770540237427})
store['active_learning_steps'][7]['eval_training']['best_epoch']=4
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 35996], ['id', 51600], ['id', 31090], ['id', 9346], ['id', 29966]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5939121632114794, 1.1196081909345716, 1.5804013375386194, 1.9470150667469452, 2.2100693769530952]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.2634658813476562})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.4769647121429443})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.5187528133392334})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.6104851961135864})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.6601111888885498})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.7181612253189087})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.6386137008666992})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.6969141960144043})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.5376253128051758})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.8068586587905884})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.759690284729004})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.786003828048706})
store['active_learning_steps'][8]['training']['best_epoch']=9
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7911, 'crossentropy': 1.41680302734375}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.150638222694397})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.1139450073242188})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.1220197677612305})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.1397931575775146})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.1465914249420166})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.0901100635528564})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.0398190021514893})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.1542251110076904})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.1537666320800781})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.1505019664764404})
store['active_learning_steps'][8]['eval_training']['best_epoch']=7
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 17257], ['id', 57431], ['id', 7541], ['id', 28470], ['id', 38785]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7044754005150229, 1.3352657494745956, 1.856730557684771, 2.227269539819071, 2.4675272227575293]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.1954686641693115})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.239781379699707})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.3406223058700562})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.4467859268188477})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.5165868997573853})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.4135704040527344})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.4860807657241821})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.7006378173828125})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.6057968139648438})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.5262782573699951})
store['active_learning_steps'][9]['training']['best_epoch']=7
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7955, 'crossentropy': 1.5048962890625}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.0510421991348267})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.101029872894287})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.0802057981491089})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.0396604537963867})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.0655076503753662})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.0876870155334473})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.0389562845230103})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.047878623008728})
store['active_learning_steps'][9]['eval_training']['best_epoch']=5
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 27859], ['id', 24010], ['id', 26022], ['id', 19038], ['id', 9448]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.863507894149879, 1.4665602851339903, 1.9388508691569464, 2.2979645063513185, 2.560830060818026]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.2025882005691528})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.3268299102783203})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.4576010704040527})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.4139816761016846})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.5420842170715332})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.422132134437561})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.4324009418487549})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.6979031562805176})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.6427645683288574})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.6521661281585693})
store['active_learning_steps'][10]['training']['best_epoch']=7
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8172, 'crossentropy': 1.35539365234375}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.0257385969161987})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.005645751953125})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9551156163215637})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.9023758172988892})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.8787336349487305})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.911363959312439})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.925631046295166})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.8740956783294678})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.8584886789321899})
store['active_learning_steps'][10]['eval_training']['best_epoch']=8
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 15947], ['id', 17015], ['id', 37811], ['id', 19124], ['id', 27181]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7305162407923278, 1.347172472542212, 1.8354036084584129, 2.18326817601288, 2.4191713424034615]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.9983277916908264})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.082481861114502})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.069528341293335})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.2443361282348633})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.2596185207366943})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.2593226432800293})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8358, 'crossentropy': 0.97819580078125}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.0385326147079468})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.02125883102417})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.8374769687652588})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.883080244064331})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.8290154337882996})
store['active_learning_steps'][11]['eval_training']['best_epoch']=5
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 51498], ['id', 23350], ['id', 35930], ['id', 23655], ['id', 26737]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.636533039961996, 1.1810219525478787, 1.5960386914973181, 1.9083190600102666, 2.1348643360459523]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.1220533847808838})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.0877327919006348})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.2263946533203125})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.3295718431472778})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.3351809978485107})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.561455488204956})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.4379442930221558})
store['active_learning_steps'][12]['training']['best_epoch']=4
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8315, 'crossentropy': 1.17925078125}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.146346092224121})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.0563417673110962})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9671108722686768})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.868489146232605})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.900536298751831})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.878616988658905})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 39381], ['id', 12109], ['id', 35903], ['id', 4040], ['id', 39461]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6064424135263703, 1.174879966950435, 1.633930587546124, 1.986780423760722, 2.2323251576217364]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.0832523107528687})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.1169514656066895})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.1681270599365234})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.2437732219696045})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.30328369140625})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.354278326034546})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.3152146339416504})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8449, 'crossentropy': 1.07552119140625}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 0.9729815721511841})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.9545463919639587})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9360604286193848})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.9505724906921387})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.83396977186203})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.8602734804153442})
store['active_learning_steps'][13]['eval_training']['best_epoch']=5
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 46271], ['id', 26017], ['id', 38747], ['id', 12514], ['id', 31703]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6233748487088333, 1.2012412879404084, 1.6603789093716643, 1.9915511027069934, 2.2009812934660893]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.02687668800354})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9580943584442139})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.007333517074585})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.972344160079956})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.0555893182754517})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.0607633590698242})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0504868030548096})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.134110450744629})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.1549607515335083})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.2797417640686035})
store['active_learning_steps'][14]['training']['best_epoch']=7
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8662, 'crossentropy': 0.9276986328125}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.0234209299087524})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8660223484039307})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8570859432220459})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7971343994140625})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7452054023742676})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.7794932126998901})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.7056463956832886})
store['active_learning_steps'][14]['eval_training']['best_epoch']=4
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 19494], ['id', 56669], ['id', 25783], ['id', 9180], ['id', 16117]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.6817504990062294, 1.2523380828524775, 1.7315800057069692, 2.076270191454671, 2.275902089335709]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.1320457458496094})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9477300643920898})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9677711725234985})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.1548709869384766})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.0899817943572998})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.131854772567749})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8547, 'crossentropy': 0.913248046875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.0159621238708496})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8512570858001709})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.7189801931381226})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.7390353679656982})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.7269662618637085})
store['active_learning_steps'][15]['eval_training']['best_epoch']=3
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 42429], ['id', 54493], ['id', 52910], ['id', 26673], ['id', 30444]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5498538246305626, 1.0683351709375817, 1.5164197600118734, 1.8664058225919513, 2.1170642514950373]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.0804411172866821})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9561112523078918})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9154398441314697})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9174702763557434})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9626771807670593})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0624380111694336})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.042693853378296})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8753, 'crossentropy': 0.79240810546875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.0193839073181152})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8650075793266296})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8199237585067749})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7344698905944824})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.7339228391647339})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7402697801589966})
store['active_learning_steps'][16]['eval_training']['best_epoch']=4
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 53006], ['id', 32766], ['ood', 38782], ['id', 54939], ['id', 50930]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5530479670890625, 1.0470964422043063, 1.4559852310539547, 1.7744830611482998, 2.0081823217956023]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.1770715713500977})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9141232967376709})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9729449152946472})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.9660147428512573})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.1087396144866943})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8611, 'crossentropy': 0.7547111328125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9320998191833496})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7407757043838501})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.7158926725387573})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7078931331634521})
store['active_learning_steps'][17]['eval_training']['best_epoch']=4
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 19942], ['id', 37137], ['id', 57523], ['id', 13627], ['id', 43126]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.665103988858335, 1.2658668764413918, 1.7258228844228922, 2.1000702426541444, 2.3506496127279615]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.9652677774429321})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8066112995147705})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.776970624923706})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8102205991744995})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9671429395675659})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9750950336456299})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8735, 'crossentropy': 0.689078076171875}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.0828475952148438})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.7999847531318665})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.7400197982788086})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.6751749515533447})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.6514166593551636})
store['active_learning_steps'][18]['eval_training']['best_epoch']=5
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 56999], ['id', 4305], ['id', 37720], ['id', 22662], ['id', 45282]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6282455726084171, 1.1485378466073728, 1.5937801898858766, 1.9182122841440306, 2.148620196274968]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.0031452178955078})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7512902021408081})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8131121397018433})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.852423906326294})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9168800115585327})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9279661178588867})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9373096227645874})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.854478120803833})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9564709663391113})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9949851632118225})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9295159578323364})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0782147645950317})
store['active_learning_steps'][19]['training']['best_epoch']=9
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8875, 'crossentropy': 0.82325908203125}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9559546113014221})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8182641267776489})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.8149410486221313})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7314531207084656})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7278075218200684})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.732576847076416})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7429196834564209})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7020520567893982})
store['active_learning_steps'][19]['eval_training']['best_epoch']=5
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 49543], ['id', 26240], ['id', 24], ['id', 52319], ['id', 54646]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.7663714624966282, 1.372634607224637, 1.8578220300775192, 2.189528637551188, 2.410116383919]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.9742258787155151})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8997718691825867})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9633471965789795})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8877811431884766})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9861690402030945})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9585630893707275})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9001337289810181})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9385086297988892})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.91150963306427})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.019175410270691})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0062607526779175})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.0681097507476807})
store['active_learning_steps'][20]['training']['best_epoch']=9
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.8877, 'crossentropy': 0.78926943359375}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9436808824539185})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7898569107055664})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7057897448539734})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6606463193893433})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7024505138397217})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.6980324983596802})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6310418844223022})
store['active_learning_steps'][20]['eval_training']['best_epoch']=4
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 17817], ['id', 25508], ['id', 42415], ['id', 33476], ['id', 517]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6680804180280793, 1.2614807042183174, 1.7565921735014198, 2.1167077024112846, 2.32599434411477]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9991062879562378})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8250325918197632})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7702272534370422})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.79012531042099})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.854202151298523})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8430932760238647})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8866, 'crossentropy': 0.688743115234375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.0024415254592896})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7282136678695679})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.6872729659080505})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.6782402992248535})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.6721659302711487})
store['active_learning_steps'][21]['eval_training']['best_epoch']=2
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 12663], ['id', 4646], ['id', 41591], ['id', 47132], ['id', 29681]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5463830765429352, 1.0565294608044788, 1.4503868273322844, 1.7176624698711391, 1.8834108359218842]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.0146962404251099})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7464114427566528})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6975751519203186})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7443076372146606})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7589375972747803})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8252050876617432})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9057, 'crossentropy': 0.58029580078125}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8890957832336426})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.6682150363922119})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.629439115524292})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5994658470153809})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.5845597386360168})
store['active_learning_steps'][22]['eval_training']['best_epoch']=4
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 10475], ['id', 24457], ['ood', 29018], ['id', 48102], ['id', 20170]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.6330099200227168, 1.1574676219557753, 1.6029935391454417, 1.921070366511219, 2.1306697276984368]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9433115720748901})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7652748823165894})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6508300304412842})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6864191889762878})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.739482045173645})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7044742107391357})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7620366811752319})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7934626936912537})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7883249521255493})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7451211214065552})
store['active_learning_steps'][23]['training']['best_epoch']=7
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9172, 'crossentropy': 0.598593798828125}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8015841245651245})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6265174150466919})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6098430156707764})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5795591473579407})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5665903687477112})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5545706152915955})
store['active_learning_steps'][23]['eval_training']['best_epoch']=3
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 12986], ['id', 4694], ['id', 5373], ['id', 38198], ['id', 58544]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7398213833887217, 1.3236199673879403, 1.8054363434671465, 2.1442823252158423, 2.365774215987619]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9220035076141357})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7137569189071655})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6811529397964478})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.707911491394043})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7278366088867188})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6604899168014526})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6716899871826172})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.733634352684021})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6976786851882935})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7299871444702148})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7989734411239624})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7517508864402771})
store['active_learning_steps'][24]['training']['best_epoch']=9
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9213, 'crossentropy': 0.571207421875}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.9459577798843384})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6803693175315857})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6027261018753052})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5576933026313782})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5696079730987549})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.534968376159668})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5465230941772461})
store['active_learning_steps'][24]['eval_training']['best_epoch']=4
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 10500], ['id', 23526], ['id', 39436], ['id', 35512], ['id', 29287]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6269715550412691, 1.1825292452693419, 1.6719484050332714, 2.068949887688651, 2.302691868652079]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9181775450706482})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6775667071342468})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6903538703918457})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6190818548202515})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7003214359283447})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6354014873504639})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6977204084396362})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.919, 'crossentropy': 0.4874267578125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9475075006484985})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6242243051528931})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5452808141708374})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5197373032569885})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5045305490493774})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.49751442670822144})
store['active_learning_steps'][25]['eval_training']['best_epoch']=6
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 14619], ['id', 42787], ['id', 47068], ['id', 25234], ['id', 8617]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5718424402749425, 1.0654787478602756, 1.4835180954337481, 1.8037352253514545, 2.034341695327064]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8833216428756714})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6044535636901855})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5780746936798096})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6744120121002197})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6384422779083252})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6503410339355469})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.704247236251831})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7419506311416626})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6882848739624023})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6813399791717529})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7820852398872375})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7708956003189087})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6876943111419678})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9843028783798218})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8046810626983643})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8633403778076172})
store['active_learning_steps'][26]['training']['best_epoch']=13
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9251, 'crossentropy': 0.55823720703125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8852783441543579})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6905911564826965})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5803589224815369})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.564365029335022})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5606979131698608})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5086560249328613})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5506142377853394})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5304172039031982})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5119301080703735})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5391522645950317})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5506123304367065})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5004945993423462})
store['active_learning_steps'][26]['eval_training']['best_epoch']=9
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 59546], ['id', 46802], ['id', 1294], ['id', 22784], ['id', 24880]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7587400711881529, 1.4475939762516123, 1.993145215792274, 2.3907572802867896, 2.6419943128319003]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9366575479507446})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6329547166824341})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6394554376602173})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5804955363273621})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6010264754295349})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6349990367889404})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.660499095916748})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9195, 'crossentropy': 0.48555908203125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9297235012054443})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6560660600662231})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5387781858444214})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5272606015205383})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.4981425702571869})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.4985657334327698})
store['active_learning_steps'][27]['eval_training']['best_epoch']=6
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 9966], ['id', 14749], ['id', 25844], ['id', 46036], ['id', 52287]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6934912384389302, 1.2815252274057696, 1.7495647401872514, 2.06998075651029, 2.2865476087674725]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9800793528556824})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6784940361976624})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6238672733306885})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6764959096908569})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6528109908103943})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6338194608688354})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.670423150062561})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7060946822166443})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7529317736625671})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7759712338447571})
store['active_learning_steps'][28]['training']['best_epoch']=7
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9274, 'crossentropy': 0.523320703125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9743021726608276})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5771234631538391})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5377703309059143})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5534783601760864})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5110695958137512})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4958389401435852})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.4886103570461273})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.4974929094314575})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.4697079360485077})
store['active_learning_steps'][28]['eval_training']['best_epoch']=6
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 32908], ['id', 36417], ['id', 25180], ['id', 15848], ['id', 21686]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.7023207643838285, 1.2953659756741858, 1.7604357289540937, 2.1134054846628816, 2.3401387869977572]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.0346518754959106})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6394197940826416})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6236894130706787})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6408490538597107})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6614915132522583})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6133061647415161})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.62932950258255})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6186854839324951})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6961901187896729})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7090753316879272})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7218770384788513})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6823276877403259})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8071645498275757})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7968056797981262})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7909531593322754})
store['active_learning_steps'][29]['training']['best_epoch']=12
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9274, 'crossentropy': 0.544807861328125}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9144251346588135})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6409975290298462})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5034090876579285})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5300720930099487})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.48767030239105225})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.46743303537368774})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.46269911527633667})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.43874967098236084})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.46419858932495117})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.45629554986953735})
store['active_learning_steps'][29]['eval_training']['best_epoch']=7
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 37129], ['ood', 3694], ['id', 37907], ['id', 20048], ['id', 11044]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6488097818146754, 1.2385513954970988, 1.7411134973213551, 2.100391770330173, 2.3223533528348943]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9512007236480713})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6415503025054932})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5700460076332092})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5735865831375122})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6191860437393188})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6397550702095032})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6212112903594971})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9302, 'crossentropy': 0.456385302734375}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.939059853553772})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5944374799728394})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.576158881187439})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5287978649139404})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5142287015914917})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.490741103887558})
store['active_learning_steps'][30]['eval_training']['best_epoch']=4
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 9804], ['id', 27029], ['id', 36515], ['id', 28693], ['id', 24531]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5711242848976188, 1.0724176224094335, 1.493036564177776, 1.8047836792920826, 2.0168992048469967]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9320781230926514})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6720445156097412})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.600886881351471})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5894739627838135})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6394600868225098})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6263641119003296})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6228495836257935})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6130462884902954})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6348884105682373})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6619517803192139})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6871556043624878})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6617646217346191})
store['active_learning_steps'][31]['training']['best_epoch']=9
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9369, 'crossentropy': 0.483945556640625}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9495111703872681})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6644515991210938})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5783485174179077})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5204886198043823})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5080251693725586})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4738835096359253})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.45128414034843445})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4746001958847046})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4574185013771057})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4390070140361786})
store['active_learning_steps'][31]['eval_training']['best_epoch']=7
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 33780], ['id', 32421], ['id', 55196], ['id', 40202], ['id', 8214]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6411347640061908, 1.2114045210143, 1.7034999978901246, 2.07125580733259, 2.302428130301019]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.030613660812378})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5973795652389526})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5460219383239746})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5280613899230957})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.568850040435791})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5515942573547363})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5637514591217041})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.559139609336853})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.634701132774353})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.579066276550293})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5927431583404541})
store['active_learning_steps'][32]['training']['best_epoch']=8
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9343, 'crossentropy': 0.45552490234375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8746012449264526})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5796035528182983})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4964824914932251})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.441956102848053})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4128984212875366})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.38937944173812866})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3977038264274597})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.44272005558013916})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4018082618713379})
store['active_learning_steps'][32]['eval_training']['best_epoch']=6
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 48723], ['id', 51207], ['id', 57419], ['id', 7083], ['id', 52861]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.7238366396616811, 1.2886777379804637, 1.77029757214153, 2.134946864606062, 2.375530035783026]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.0321218967437744})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5939914584159851})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4873594641685486})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4817274212837219})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.45475733280181885})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.46780434250831604})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4934222102165222})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5662705898284912})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.49457818269729614})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5257114768028259})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5738421678543091})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5743101835250854})
store['active_learning_steps'][33]['training']['best_epoch']=9
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9427, 'crossentropy': 0.3968490966796875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.0515227317810059})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5709954500198364})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5290936231613159})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4879841208457947})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4981953501701355})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4571578800678253})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.43859249353408813})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4300287067890167})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4357995092868805})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4211723208427429})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.42234766483306885})
store['active_learning_steps'][33]['eval_training']['best_epoch']=8
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 3094], ['id', 37605], ['id', 15963], ['id', 19472], ['id', 32769]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6403377627515454, 1.2117256054255505, 1.671313754783092, 2.0425686633295865, 2.3504135144694405]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9410622119903564})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5751707553863525})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5092412233352661})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5611534118652344})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5314400792121887})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5472031831741333})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5041301846504211})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5208675265312195})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5668272972106934})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5564404129981995})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5347562432289124})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5822699666023254})
store['active_learning_steps'][34]['training']['best_epoch']=9
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9397, 'crossentropy': 0.449085107421875}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8564878702163696})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5549657344818115})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5066075325012207})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.48372071981430054})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.429563045501709})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4504399299621582})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.44938188791275024})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.43192675709724426})
store['active_learning_steps'][34]['eval_training']['best_epoch']=5
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 21601], ['id', 10992], ['id', 424], ['id', 36421], ['id', 47915]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6806713882811894, 1.257278132569732, 1.7326291718696845, 2.0505864181923252, 2.217990465828138]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.0192534923553467})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6326836943626404})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6027406454086304})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.550567626953125})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5019330978393555})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5963349342346191})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6003959774971008})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5623629093170166})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6124627590179443})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5251369476318359})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5675284266471863})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5886737704277039})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6495170593261719})
store['active_learning_steps'][35]['training']['best_epoch']=10
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9398, 'crossentropy': 0.434691943359375}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9172707796096802})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.551978349685669})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.49951690435409546})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5170918703079224})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.45678919553756714})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4765015244483948})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.48721081018447876})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4746696949005127})
store['active_learning_steps'][35]['eval_training']['best_epoch']=5
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 670], ['id', 43169], ['id', 10044], ['id', 38302], ['id', 18122]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.5867826078043048, 1.1476431787692212, 1.5850960192550283, 1.9158610579357962, 2.1440968911489167]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9560158252716064})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6197860240936279})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5018163919448853})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5733591318130493})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5485976934432983})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.536303699016571})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.521916389465332})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5374445915222168})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5258964896202087})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5829917192459106})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5916701555252075})
store['active_learning_steps'][36]['training']['best_epoch']=8
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9381, 'crossentropy': 0.443752099609375}
